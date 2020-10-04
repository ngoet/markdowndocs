from dataclasses import dataclass
from typing import List, Optional


class FILE:
    """Constants for input/output files"""

    OUTPUT_DEFAULT = "code_documentation.md"
    INPUT_DEFAULT = "README.md"
    DEFAULT_HEADER = "Code documentation"
    NAVIGATION = "&uparrow; Back to"
    DOCUMENTATION_REF = "\n## Code documentation\n[Code documentation](code_documentation.md)"
    PACKAGE_NAME = "markdowndocs"


@dataclass
class FunctionObject:
    """A FunctionObject object"""

    function_name: str
    function_description: Optional[str]
    code: Optional[str]


@dataclass
class MarkdownClassObject:
    """A MarkdownFunctionObject object"""

    class_name: str
    class_description: str
    function_objects: List[FunctionObject]


@dataclass
class MarkDownModuleObject:
    """A MarkdownFunctionObject object"""

    module: str
    module_description: Optional[str]
    dependencies: Optional[List[str]]
    function_markdown_objects: List[FunctionObject]
    class_markdown_objects: List[MarkdownClassObject]


@dataclass
class Module:
    """A Module object"""

    name: str
    path: str
