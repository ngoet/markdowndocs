import argparse

import typer

from markdowndocs import constants as c
from markdowndocs import version
from markdowndocs.mddocs import check_md_file, generate_markdown_file, identify_modules


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
        help="If enabled, excludes the source code for each function." "\n[default: False]",
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


if __name__ == "__main__":
    main()
