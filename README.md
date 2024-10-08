# MarkdownDocs

[![](https://img.shields.io/pypi/v/markdowndocs.svg)](https://pypi.org/project/markdowndocs/)
[![Downloads](https://pepy.tech/badge/markdowndocs)](https://pepy.tech/project/markdowndocs)
[![Downloads](https://pepy.tech/badge/markdowndocs/month)](https://pepy.tech/project/markdowndocs/month)
[![license](https://img.shields.io/github/license/ngoet/markdowndocs)](https://github.com/ngoet/markdowndocs/blob/main/LICENSE)

[![ci-linting](https://github.com/ngoet/markdowndocs/actions/workflows/ci-linting.yaml/badge.svg?branch=main)](https://github.com/ngoet/markdowndocs/actions/workflows/ci-linting.yaml)
[![ci-regression-tests](https://github.com/ngoet/markdowndocs/actions/workflows/ci-regression-tests.yaml/badge.svg?branch=main)](https://github.com/ngoet/markdowndocs/actions/workflows/ci-regression-tests.yaml)
[![ci-unit-tests](https://github.com/ngoet/markdowndocs/actions/workflows/ci-unit-tests.yaml/badge.svg?branch=main)](https://github.com/ngoet/markdowndocs/actions/workflows/ci-unit-tests.yaml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

`markdowndocs` is a light-weight markdown documentation generator that generates a simple `.md` file that documents your Python code based on your docstrings and source code.

---

[Installation and usage](#installation-and-usage) | [Usage](#usage) | [Using markdowndocs with pre-commit](#using-markdowndocs-with-pre-commit-hooks-version-control-integration) | [Contributor guidelines](#contributor-guidelines) | [Code documentation](#code-documentation)

---

## Installation and usage

### Installation
Install with:
```
pip install markdowndocs
```

### Usage
#### Options
To run `markdowndocs` on all modules in your working directory:
```bash
$ markdowndocs --all
```

To run `markdowndocs` on (a) specific module(s) in your working directory:
```bash
$ markdowndocs --module-names <my_module>
```

To run `markdowndocs` on on all modules in your working directory, *except* (a) specific module(s):
```bash
$ markdowndocs --exclude-modules <my_module>
```

Full options and use:
```text
$ markdowndocs --help
usage: markdowndocs [-h] [--output-file-name NAME] [--add-to-readme]
                    [--exclude-dependencies] [--exclude-code] [--version]
                    (-a | -m NAME [NAME ...] | -e NAME [NAME ...])

Markdown documentation package.

optional arguments:
  -h, --help            show this help message and exit
  --output-file-name NAME
                        Use this option to specify a custom output file name
                        for the .md documentation [default:
                        code_documentation.md]
  --add-to-readme       If enabled, adds a link to your documentation file to
                        your README.md file with the following format: ## Code
                        documentation [Code
                        Documentation](code_documentation.md) [default: False]
  --exclude-dependencies
                        If enabled, includes a list of dependencies for each
                        module. [default: False]
  --exclude-code        If enabled, excludes the source code for each function.
                        [default: False]
  --version             Show version information and exit.
  -a, --all             Use this option to generate documentation for all
                        modules in your current working directory [default:
                        False]
  -m NAME [NAME ...], --module-names NAME [NAME ...]
                        Use this option to generate documentation for a
                        specific module or modules
  -e NAME [NAME ...], --exclude-modules NAME [NAME ...]
                        Use this option to exclude a specific module or
                        multiple modules from the documentation generator
```
#### Output
By default, the generated markdown documentation is stored in a file called `code_documentation.md`. You can use the `--output-file-name` argument to set a custom file name.
The following is included in the output by default:
* User-defined docstrings for modules, classes, and functions (including private methods);
* Internal links and nested tables of content for all modules, classes, and functions;
* A list of dependencies (i.e. imports) for each module;
* The source code for each function.

#### Examples
Markdowndocs output for:
* [a single function](examples/one_function.md)
* [multiple_functions](examples/multiple_functions.md)
* [class and functions](examples/class_and_functions.md)
* [class and private functions](examples/class_and_private_functions.md)
* [multiple_modules](examples/multiple_modules.md)
* [markdowndocs code documentation](examples/code_documentation.md)

### Known limitations
* `markdowndocs` will only pick up modules in directories in your working directory, but not in sub-directories (i.e. only one level of "nestedness" is currently supported)
* `markdowndocs` assumes that all imports in your code work, that is, do not refer to non-existing modules.
* `markdowndocs` does not play nicely with [pydantic](https://pydantic-docs.helpmanual.io/).

## Using `markdowndocs` with pre-commit hooks
To use `markdowndocs` to generate up-to-date documentation upon every new commit, add the following configuration to your `.pre-commit-config.yaml` file (and add your preferred configuration options in the `args` field):

```buildoutcfg
repos:
-   repo: https://github.com/ngoet/markdowndocs
    rev: 0.1.0
    hooks:
    - id: markdowndocs
      pass_filenames: false
      args: ["-m", "<my-module-name>",
             "--add-to-readme"]
```

## Contributor guidelines
Suggestions for improvements are appreciated. Please open an issue if you find anything is broken, or if you'd like to suggest changes.

## Code documentation
[Code documentation](examples/code_documentation.md)
