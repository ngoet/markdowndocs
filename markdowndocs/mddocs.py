import importlib
import inspect
import os
import sys
from contextlib import contextmanager
from os.path import basename, isdir, isfile
from pathlib import Path
from typing import List, Tuple, Union

import typer

from markdowndocs import constants as c
from markdowndocs.constants import FunctionObject, MarkdownClassObject, MarkDownModuleObject, Module
from markdowndocs.md_utils import add_header, add_index, add_python_snippet, gen_anchor, list_to_md


@contextmanager
def load_from_wd():
    """
    Load from working directory.

    Context manager that ensures we only read files from the current WD.
    """
    dir_ = Path.cwd()
    import_path0 = sys.path[0]
    sys.path[0] = str(dir_)

    try:
        yield
    finally:
        sys.path[0] = import_path0


def _module_exist_error(identified_modules: List[Module], mod_name: str) -> None:
    """
    Check if a module with a user-specified name exists; raise an error if not.

    :param identified_modules: A list of identified modules in the wd.
    :param mod_name: The user-specified module name.
    """
    names = [i.name for i in identified_modules]
    sep = "\n - "
    if mod_name not in names:
        typer.secho(
            f"\nModule {mod_name} not found. Process aborted."
            "\n-------------------------------------------\n"
            f"\n{c.FILE.PACKAGE_NAME} found the following modules in your wd: \n - {sep.join(names)}",
            bold=True,
        )
        os._exit(1)


def gen_real_path(pth: str) -> str:
    """
    Generate absolute filesytem path.

    :param pth: Input path / name.
    :return: Absolute filesytem path.
    """
    for f in [os.path.expanduser, os.path.normpath, os.path.realpath, os.path.abspath]:
        pth = f(pth)
    return pth + ".py"


def _extract_function_information(
    functions: List[Tuple[str, callable]], module: callable, args, condition: str
) -> List[FunctionObject]:
    """
    Extract function information.

    :param functions: A list of functions in the module.
    :param module: An imported module.
    :param args: User-specified options.
    :param condition: A string value that the module name needs to meet in order to be included in the markdown object.
    :return: A list of populated objects conforming with FunctionObject.
    """
    function_objects = []

    # __init__ order is not preserved in the case of classes with private methods.
    fnames = [i[0] for i in functions]
    if "__init__" in fnames:
        fnames.remove("__init__")
        fnames.insert(0, "__init__")
        functions = [i for j in fnames for i in filter(lambda k: k[0] == j, functions)]

    for f in functions:
        if str(f[1].__module__) == condition:
            function_object = FunctionObject(
                function_name=f[1].__qualname__, function_description=f[1].__doc__, code=None
            )

            if not args.exclude_code:
                function_object.code = inspect.getsource(getattr(module, f[0]))

            function_objects.append(function_object)
    return function_objects


def get_class_attributes(obj) -> List[str]:
    """
    Function to obtain the values of all attributes of a class.

    :param obj: A tmp ingestion constants class
    :return: A list containing the values of all attributes associated with the class.
    """
    class_objects = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    return [getattr(obj, i) for i in class_objects]


def process_module(mod: Union[Module, str], args) -> MarkDownModuleObject:
    """
    Process module.

    Processes the functions and docstrings in the module, and adds this information to a MarkDownModuleObject instance.

    :param mod: The module that will be processed.
    :param args: argparse.Namespace from the CLI.
    :return: An object conforming with MarkDownModuleObject.
    """

    if isinstance(mod, str):
        with load_from_wd():
            my_module = importlib.import_module(mod)
    else:
        spec = importlib.util.spec_from_file_location(mod.name, gen_real_path(mod.name))
        my_module = importlib.util.module_from_spec(spec)
        with load_from_wd():
            spec.loader.exec_module(my_module)

    markdown_module_object = MarkDownModuleObject(
        module=my_module.__name__,
        module_description=my_module.__doc__,
        class_markdown_objects=[],
        function_markdown_objects=[],
        dependencies=[],
    )

    # Include information on dependencies
    if not args.exclude_dependencies:
        markdown_module_object.dependencies = [i[1].__name__ for i in inspect.getmembers(my_module, inspect.ismodule)]

    # Identify classes
    module_classes = [
        myclass
        for myclass in inspect.getmembers(my_module, inspect.isclass)
        if str(myclass[1].__module__) == my_module.__name__
    ]

    # Process classes (if present)
    if module_classes:
        for myclass in module_classes:

            class_markdown_object = MarkdownClassObject(
                class_name=myclass[1].__name__, class_description=myclass[1].__doc__, function_objects=[]
            )

            functions = inspect.getmembers(myclass[1], inspect.isfunction)
            class_markdown_object.function_objects += _extract_function_information(
                module=myclass[1], args=args, functions=functions, condition=myclass[1].__module__
            )
            markdown_module_object.class_markdown_objects.append(class_markdown_object)

    # Identify non-class functions
    functions = inspect.getmembers(my_module, inspect.isfunction)
    markdown_module_object.function_markdown_objects += _extract_function_information(
        module=my_module, args=args, functions=functions, condition=my_module.__name__
    )

    return markdown_module_object


def convert_markdown_module_object_to_markdown(markdown_module_object: MarkDownModuleObject) -> str:
    """
    Convert a MarkDownModuleObject instance into markdown syntax.

    :param markdown_module_object: An object conforming with MarkDownModuleObject.
    :return: A string of markdown syntax.
    """
    md_string = ""
    md_string += add_header(level=2, header_text=markdown_module_object.module)
    md_string += f"\n{c.FILE.NAVIGATION} [code documentation index](#{gen_anchor(c.FILE.DEFAULT_HEADER)})\n"

    if markdown_module_object.dependencies:
        md_string += list_to_md(
            items=markdown_module_object.dependencies, introductory_text=add_header(3, "Dependencies")
        )

    if markdown_module_object.class_markdown_objects:
        md_string += add_header(level=3, header_text="Classes")
        md_string += add_index([my_class.class_name for my_class in markdown_module_object.class_markdown_objects])
        for my_class in markdown_module_object.class_markdown_objects:
            md_string += add_header(level=4, header_text=my_class.class_name)
            md_string += (
                f"\n{my_class.class_description}" if my_class.class_description else "\n*No docstrings available.*"
            )
            if my_class.function_objects:
                md_string += add_header(level=5, header_text="Functions")
                md_string += add_index([f"{i.function_name}" for i in my_class.function_objects])
                for entry in my_class.function_objects:
                    md_string += add_header(level=6, header_text=f"{entry.function_name}")
                    md_string += (
                        f"\n{c.FILE.NAVIGATION} [code documentation index](#{gen_anchor(c.FILE.DEFAULT_HEADER)})\n"
                    )
                    md_string += f"\n{c.FILE.NAVIGATION} [module index](#{markdown_module_object.module})\n"
                    md_string += f"\n{c.FILE.NAVIGATION} [class index](#{my_class.class_name})\n"
                    md_string += (
                        f"\n{entry.function_description}"
                        if entry.function_description
                        else "\n*No docstrings available.*"
                    )
                    if entry.code:
                        md_string += add_python_snippet(entry.code)

    if markdown_module_object.function_markdown_objects:
        md_string += add_header(level=3, header_text="Functions")
        md_string += add_index([i.function_name for i in markdown_module_object.function_markdown_objects])

        for entry in markdown_module_object.function_markdown_objects:
            md_string += add_header(level=4, header_text=entry.function_name)
            md_string += f"\n{c.FILE.NAVIGATION} [code documentation index](#{gen_anchor(c.FILE.DEFAULT_HEADER)})\n"
            md_string += f"\n{c.FILE.NAVIGATION} [module index](#{markdown_module_object.module})\n"
            md_string += (
                f"\n{entry.function_description}" if entry.function_description else "\n*No docstrings available.*"
            )
            if entry.code:
                md_string += add_python_snippet(entry.code)

    return md_string


def identify_modules(args) -> List[Module]:
    """
    Identify modules.

    :param args: User-specified arguments.
    :return: a list of module names and full paths in the current directory.
    """

    mods = os.listdir()

    identified_modules = [
        Module(name=basename(f)[:-3], path=f)
        for f in mods
        if isfile(f) and f.endswith(".py") and not f.endswith("__.py")
    ]

    dirs = [i for i in mods if isdir(i)]
    for dir in dirs:
        mods = [os.path.join(dir, i) for i in os.listdir(dir)]
        identified_modules += [
            Module(name=f"{dir}/{basename(f)[:-3]}", path=f)
            for f in mods
            if isfile(f) and f.endswith(".py") and not f.endswith("__.py")
        ]

    if args.module_names:
        module_names = [x.replace(".py", "") for x in args.module_names]
        for mod_name in module_names:
            if mod_name not in [i.name for i in identified_modules]:
                _module_exist_error(identified_modules, mod_name)
        identified_modules = [i for i in identified_modules if i.name in module_names]

    if args.exclude_modules:
        module_names = [x.replace(".py", "") for x in args.exclude_modules]
        for mod_name in module_names:
            if mod_name not in [i.name for i in identified_modules]:
                _module_exist_error(identified_modules, mod_name)
        identified_modules = [i for i in identified_modules if i.name not in module_names]

    if not identified_modules:
        typer.secho(f"\nNo Python modules found in current wd. Process aborted.", bold=True)
        os._exit(1)

    return identified_modules


def generate_markdown_file(args, modules: List[Module], output_file_name: str) -> None:
    """
    Generate markdown file.

    :param args: User-specified arguments.
    :param modules: A list of (selected) modules in the wd.
    :param output_file_name: The output file name for the .md file.
    """
    mod_obj = [process_module(mod, args) for mod in modules]

    md_string = ""
    md_string += add_header(1, c.FILE.DEFAULT_HEADER)

    # Construct hierarchical index
    for mod in mod_obj:
        md_string += add_index([mod.module])  # Add module link
        if mod.class_markdown_objects:
            for m in mod.class_markdown_objects:
                md_string += add_index([m.class_name], 1)  # Add class link
                for myclass in m.function_objects:
                    md_string += add_index([f"{myclass.function_name}"], 2)  # Add class.function link

        if mod.function_markdown_objects:
            for f in mod.function_markdown_objects:
                md_string += add_index([f.function_name], 1)  # Add function link

    for mod in mod_obj:
        md_string += convert_markdown_module_object_to_markdown(mod)

    if args.add_to_readme:
        if os.path.exists("README.md"):
            with open("README.md", "r") as readme:
                readme_file = readme.read()
                readme.close()
                if c.FILE.DOCUMENTATION_REF not in readme_file:
                    readme_file += c.FILE.DOCUMENTATION_REF
                    with open("README.md", "w") as readme:
                        readme.write(readme_file)
        else:
            typer.secho(
                "No README.md found in current wd. --add-to-readme option ignored", bold=True, fg=typer.colors.YELLOW
            )

    with open(output_file_name, "w") as doc:
        doc.write(md_string)


def check_md_file(md_file_name: str) -> str:
    """
    Check markdown (md) file.

    Checks that the provided file has a .md extension.

    :param md_file_name: A string
    :return: the md file name.
    """
    if md_file_name and ".md" not in md_file_name:
        md_file_name += ".md"
    return md_file_name
