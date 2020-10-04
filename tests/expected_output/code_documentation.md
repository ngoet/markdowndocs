# <a name='codedocumentation'></a>Code documentation

* [md\_utils](#mdutils)


	* [add\_custom\_header\_anchor](#addcustomheaderanchor)


	* [add\_header](#addheader)


	* [add\_index](#addindex)


	* [add\_python\_snippet](#addpythonsnippet)


	* [add\_table](#addtable)


	* [gen\_anchor](#genanchor)


	* [italicize](#italicize)


	* [list\_to\_md](#listtomd)


* [mddocs](#mddocs)


	* [\_extract\_function\_information](#extractfunctioninformation)


	* [\_module\_exist\_error](#moduleexisterror)


	* [check\_md\_file](#checkmdfile)


	* [convert\_markdown\_module\_object\_to\_markdown](#convertmarkdownmoduleobjecttomarkdown)


	* [gen\_real\_path](#genrealpath)


	* [generate\_markdown\_file](#generatemarkdownfile)


	* [get\_class\_attributes](#getclassattributes)


	* [identify\_modules](#identifymodules)


	* [load\_from\_wd](#loadfromwd)


	* [process\_module](#processmodule)


* [constants](#constants)


	* [FILE](#file)


	* [FunctionObject](#functionobject)


	* [MarkDownModuleObject](#markdownmoduleobject)


	* [MarkdownClassObject](#markdownclassobject)


	* [Module](#module)


* [cli](#cli)


	* [main](#main)


	* [set\_up\_parser](#setupparser)

## <a name='mdutils'></a>md\_utils
&uparrow; Back to [code documentation index](#codedocumentation)


### <a name='dependencies'></a>Dependencies
* pandas

* re

* string

### <a name='functions'></a>Functions

* [add\_custom\_header\_anchor](#addcustomheaderanchor)

* [add\_header](#addheader)

* [add\_index](#addindex)

* [add\_python\_snippet](#addpythonsnippet)

* [add\_table](#addtable)

* [gen\_anchor](#genanchor)

* [italicize](#italicize)

* [list\_to\_md](#listtomd)

#### <a name='addcustomheaderanchor'></a>add\_custom\_header\_anchor
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Add custom header anchor.

    :param txt: A string object.
    :return: html syntax for a header anchor.

<details>
<summary>raw code</summary>

```python
def add_custom_header_anchor(txt: str) -> str:
    """
    Add custom header anchor.

    :param txt: A string object.
    :return: html syntax for a header anchor.
    """
    return f"<a name='{gen_anchor(txt)}'></a>"

```
</details>

#### <a name='addheader'></a>add\_header
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Add header.

    :param level: The header level.
    :param header_text: String object containing the header text.
    :return: Header markdown syntax.

<details>
<summary>raw code</summary>

```python
def add_header(level: int, header_text: str) -> str:
    """
    Add header.

    :param level: The header level.
    :param header_text: String object containing the header text.
    :return: Header markdown syntax.
    """
    assert level <= 6, "Header level cannot exceed 4"

    prefix = "" if level == 1 else "\n"
    backslash = "\_"
    return f"{prefix}{'#' * level} {add_custom_header_anchor(header_text)}{re.sub('_', backslash, header_text)}"

```
</details>

#### <a name='addindex'></a>add\_index
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Add index.

    :param headers: A list of header strings.
    :param indent: The indentation level for the link.
    :return: Markdown syntax for an index.

<details>
<summary>raw code</summary>

```python
def add_index(headers: List[str], indent: int = 0) -> str:
    """
    Add index.

    :param headers: A list of header strings.
    :param indent: The indentation level for the link.
    :return: Markdown syntax for an index.
    """
    backslash = "\_"
    return list_to_md([f"[{re.sub('_', backslash, h)}](#{gen_anchor(h)})" for h in headers], indent=indent)

```
</details>

#### <a name='addpythonsnippet'></a>add\_python\_snippet
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Add a python snippet.

    :param txt: A string object.
    :param expandable: If true, puts code in <details></details> syntax.
    :return: Python string markdown syntax.

<details>
<summary>raw code</summary>

```python
def add_python_snippet(txt: str, expandable: bool = True):
    """
    Add a python snippet.

    :param txt: A string object.
    :param expandable: If true, puts code in <details></details> syntax.
    :return: Python string markdown syntax.
    """
    md_str = f"\n```python\n{txt}\n```"

    if expandable:
        md_str = f"\n<details>\n<summary>raw code</summary>\n{md_str}\n</details>\n"

    return md_str

```
</details>

#### <a name='addtable'></a>add\_table
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Add table.

    :param df: A pandas dataframe.
    :return: Table markdown syntax.

<details>
<summary>raw code</summary>

```python
def add_table(df: pd.DataFrame) -> str:
    """
    Add table.

    :param df: A pandas dataframe.
    :return: Table markdown syntax.
    """
    return tabulate(df, tablefmt="pipe", headers="keys", showindex=False)

```
</details>

#### <a name='genanchor'></a>gen\_anchor
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Generate anchor.

    Generates an anchor for a title (for internal links).

    :param txt: A string object.
    :return: A hyphen-separated string.

<details>
<summary>raw code</summary>

```python
def gen_anchor(txt: str) -> str:
    """
    Generate anchor.

    Generates an anchor for a title (for internal links).

    :param txt: A string object.
    :return: A hyphen-separated string.
    """
    regex = re.compile("[%s+| ]" % re.escape(string.punctuation))
    return regex.sub("", txt.lower())

```
</details>

#### <a name='italicize'></a>italicize
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    Italicize.

    :param txt: A string object.
    :return: Italicized string markdown syntax.

<details>
<summary>raw code</summary>

```python
def italicize(txt: str):
    """
    Italicize.

    :param txt: A string object.
    :return: Italicized string markdown syntax.
    """
    return "\n*" + " ".join(txt.replace("\n", "").split()) + "*\n"

```
</details>

#### <a name='listtomd'></a>list\_to\_md
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#md_utils)


    List to markdown.

    Convert a list of strings to a markdown list of items.

    :param items: A list of items.
    :param introductory_text: A string that is used to preface the list.
    :param list_st: Markdown bullet point string (* ).
    :param indent: The indentation level.
    :return: Markdown syntax for a list of bullet points.

<details>
<summary>raw code</summary>

```python
def list_to_md(
    items: List[str], introductory_text: str = None, list_st: str = "\n{indent}* {txt}\n", indent: int = 0
) -> str:
    """
    List to markdown.

    Convert a list of strings to a markdown list of items.

    :param items: A list of items.
    :param introductory_text: A string that is used to preface the list.
    :param list_st: Markdown bullet point string (* ).
    :param indent: The indentation level.
    :return: Markdown syntax for a list of bullet points.
    """
    md_string = "\n"
    if introductory_text is not None:
        md_string += introductory_text

    for x in items:
        md_string += list_st.format(indent="\t" * indent, txt=x)

    return md_string

```
</details>

## <a name='mddocs'></a>mddocs
&uparrow; Back to [code documentation index](#codedocumentation)


### <a name='dependencies'></a>Dependencies
* markdowndocs.constants

* importlib

* inspect

* os

* sys

* typer

### <a name='functions'></a>Functions

* [\_extract\_function\_information](#extractfunctioninformation)

* [\_module\_exist\_error](#moduleexisterror)

* [check\_md\_file](#checkmdfile)

* [convert\_markdown\_module\_object\_to\_markdown](#convertmarkdownmoduleobjecttomarkdown)

* [gen\_real\_path](#genrealpath)

* [generate\_markdown\_file](#generatemarkdownfile)

* [get\_class\_attributes](#getclassattributes)

* [identify\_modules](#identifymodules)

* [load\_from\_wd](#loadfromwd)

* [process\_module](#processmodule)

#### <a name='extractfunctioninformation'></a>\_extract\_function\_information
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Extract function information.

    :param functions: A list of functions in the module.
    :param module: An imported module.
    :param args: User-specified options.
    :param condition: A string value that the module name needs to meet in order to be included in the markdown object.
    :return: A list of populated objects conforming with FunctionObject.

<details>
<summary>raw code</summary>

```python
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
            function_object = FunctionObject(function_name=f[1].__qualname__, function_description=f[1].__doc__, code=None)

            if not args.exclude_code:
                # function_name = f[1].__qualname__.replace(".", "") if f[1].__qualname__.replace(f[1].__module__, "").startswith("_") else f[1].__qualname__
                function_object.code = inspect.getsource(getattr(module, f[0]))

            function_objects.append(function_object)
    return function_objects

```
</details>

#### <a name='moduleexisterror'></a>\_module\_exist\_error
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Check if a module with a user-specified name exists; raise an error if not.

    :param identified_modules: A list of identified modules in the wd.
    :param mod_name: The user-specified module name.

<details>
<summary>raw code</summary>

```python
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

```
</details>

#### <a name='checkmdfile'></a>check\_md\_file
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Check markdown (md) file.

    Checks that the provided file has a .md extension.

    :param md_file_name: A string
    :return: the md file name.

<details>
<summary>raw code</summary>

```python
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

```
</details>

#### <a name='convertmarkdownmoduleobjecttomarkdown'></a>convert\_markdown\_module\_object\_to\_markdown
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Convert a MarkDownModuleObject instance into markdown syntax.

    :param markdown_module_object: An object conforming with MarkDownModuleObject.
    :return: A string of markdown syntax.

<details>
<summary>raw code</summary>

```python
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
                # md_string += add_index([f"{my_class.class_name}.{i.function_name}" for i in my_class.function_objects])
                for entry in my_class.function_objects:
                    md_string += add_header(level=6, header_text=f"{entry.function_name}")
                    # md_string += add_header(level=6, header_text=f"{my_class.class_name}.{entry.function_name}")
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

```
</details>

#### <a name='genrealpath'></a>gen\_real\_path
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Generate absolute filesytem path.

    :param pth: Input path / name.
    :return: Absolute filesytem path.

<details>
<summary>raw code</summary>

```python
def gen_real_path(pth: str) -> str:
    """
    Generate absolute filesytem path.

    :param pth: Input path / name.
    :return: Absolute filesytem path.
    """
    for f in [os.path.expanduser, os.path.normpath, os.path.realpath, os.path.abspath]:
        pth = f(pth)
    return pth + ".py"

```
</details>

#### <a name='generatemarkdownfile'></a>generate\_markdown\_file
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Generate markdown file.

    :param args: User-specified arguments.
    :param modules: A list of (selected) modules in the wd.
    :param output_file_name: The output file name for the .md file.

<details>
<summary>raw code</summary>

```python
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
                    # md_string += add_index([f"{m.class_name}.{myclass.function_name}"], 2)  # Add class.function link
                    md_string += add_index([f"{myclass.function_name}"], 2)  # Add class.function link

        if mod.function_markdown_objects:
            for f in mod.function_markdown_objects:
                md_string += add_index([f.function_name], 1)  # Add function link

    for mod in mod_obj:
        md_string += convert_markdown_module_object_to_markdown(mod)

    if args.add_to_readme:
        with open("README.md", "r") as readme:
            readme_file = readme.read()
            readme.close()
            if c.FILE.DOCUMENTATION_REF not in readme_file:
                readme_file += c.FILE.DOCUMENTATION_REF
                with open("README.md", "w") as readme:
                    readme.write(readme_file)
    with open(output_file_name, "w") as doc:
        doc.write(md_string)

```
</details>

#### <a name='getclassattributes'></a>get\_class\_attributes
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Function to obtain the values of all attributes of a class.

    :param obj: A tmp ingestion constants class
    :return: A list containing the values of all attributes associated with the class.

<details>
<summary>raw code</summary>

```python
def get_class_attributes(obj) -> List[str]:
    """
    Function to obtain the values of all attributes of a class.

    :param obj: A tmp ingestion constants class
    :return: A list containing the values of all attributes associated with the class.
    """
    class_objects = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    return [getattr(obj, i) for i in class_objects]

```
</details>

#### <a name='identifymodules'></a>identify\_modules
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Identify modules.

    :param args: User-specified arguments.
    :return: a list of module names and full paths in the current directory.

<details>
<summary>raw code</summary>

```python
def identify_modules(args) -> List[Module]:
    """
    Identify modules.

    :param args: User-specified arguments.
    :return: a list of module names and full paths in the current directory.
    """

    mods = os.listdir()

    # Support 1 level of recursion
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

```
</details>

#### <a name='loadfromwd'></a>load\_from\_wd
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Load from working directory.

    Context manager that ensures we only read files from the current WD.

<details>
<summary>raw code</summary>

```python
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

```
</details>

#### <a name='processmodule'></a>process\_module
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#mddocs)


    Process module.

    Processes the functions and docstrings in the module, and adds this information to a MarkDownModuleObject instance.

    :param mod: The module that will be processed.
    :param args: argparse.Namespace from the CLI.
    :return: An object conforming with MarkDownModuleObject.

<details>
<summary>raw code</summary>

```python
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

```
</details>

## <a name='constants'></a>constants
&uparrow; Back to [code documentation index](#codedocumentation)

### <a name='classes'></a>Classes

* [FILE](#file)

* [FunctionObject](#functionobject)

* [MarkDownModuleObject](#markdownmoduleobject)

* [MarkdownClassObject](#markdownclassobject)

* [Module](#module)

#### <a name='file'></a>FILE
Constants for input/output files
#### <a name='functionobject'></a>FunctionObject
A FunctionObject object
#### <a name='markdownmoduleobject'></a>MarkDownModuleObject
A MarkdownFunctionObject object
#### <a name='markdownclassobject'></a>MarkdownClassObject
A MarkdownFunctionObject object
#### <a name='module'></a>Module
A Module object
## <a name='cli'></a>cli
&uparrow; Back to [code documentation index](#codedocumentation)


### <a name='dependencies'></a>Dependencies
* argparse

* markdowndocs.constants

* typer

### <a name='functions'></a>Functions

* [main](#main)

* [set\_up\_parser](#setupparser)

#### <a name='main'></a>main
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#cli)


    Main module for CLI.

    :param _args: parser arguments.

<details>
<summary>raw code</summary>

```python
def main(_args=None) -> None:
    """
    Main module for CLI.

    :param _args: parser arguments.
    """
    parser = set_up_parser()
    args = _args or parser.parse_args()

    # Process modules in directory / user-supplied module.
    modules = identify_modules(args)
    output_file_name = check_md_file(args.output_file_name)
    generate_markdown_file(args=args, modules=modules, output_file_name=output_file_name)

    prefix = "\n -"
    typer.secho(
        f"\n"
        f"Processed modules: "
        f"\n-------------------\n"
        f"\n -{prefix.join([mod.name for mod in modules])}\n"
        f"\n-------------------\n"
        f"Output file: {output_file_name}",
        bold=True,
    )
    typer.Exit()

```
</details>

#### <a name='setupparser'></a>set\_up\_parser
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#cli)


    Set up the arg. parser for the CLI.

    :return parser: argparse.ArgumentParser object.

<details>
<summary>raw code</summary>

```python
def set_up_parser() -> argparse.ArgumentParser:
    """
    Set up the arg. parser for the CLI.

    :return parser: argparse.ArgumentParser object.
    """
    parser = argparse.ArgumentParser(prog="markdowndocs", description="Markdown documentation package.")
    add_arg = parser.add_argument
    add_arg(
        "--output-file-name",
        metavar="NAME",
        type=str,
        help=f"Use this option to specify a custom output file name for the .md documentation "
        f"\n[default: {c.FILE.OUTPUT_DEFAULT}]",
        default=c.FILE.OUTPUT_DEFAULT,
    )
    add_arg(
        "--add-to-readme",
        action="store_true",
        help="If enabled, adds a link to your documentation file to your README.md file with the following format:"
        "\n## Code documentation"
        "\n[Code Documentation](code_documentation.md)"
        "\n[default: False]",
    )
    add_arg(
        "--exclude-dependencies",
        action="store_true",
        help="If enabled, includes a list of dependencies for each module." "\n[default: False]",
    )
    add_arg(
        "--exclude-code",
        action="store_true",
        help="If enabled, excludes the raw code for each function." "\n[default: False]",
    )
    add_arg(
        "--version",
        action="version",
        version=f"{c.FILE.PACKAGE_NAME}_{version}",
        help="Show version information and exit.",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Use this option to generate documentation for all modules in your current working directory "
        f"\n[default: False]",
    )
    group.add_argument(
        "-m",
        "--module-names",
        metavar="NAME",
        nargs="+",
        type=str,
        help="Use this option to generate documentation for a specific module or modules ",
    )
    group.add_argument(
        "-e",
        "--exclude-modules",
        metavar="NAME",
        nargs="+",
        type=str,
        help="Use this option to exclude a specific module or multiple modules from the documentation generator",
    )
    return parser

```
</details>
