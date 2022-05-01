import re
import string
from typing import List

import pandas as pd
from tabulate import tabulate


def gen_anchor(txt: str) -> str:
    """
    Generate anchor.

    Generates an anchor for a title (for internal links).

    :param txt: A string object.
    :return: A hyphen-separated string.
    """
    regex = re.compile("[%s+| ]" % re.escape(string.punctuation))
    return regex.sub("", txt.lower())


def add_custom_header_anchor(txt: str) -> str:
    """
    Add custom header anchor.

    :param txt: A string object.
    :return: html syntax for a header anchor.
    """
    return f"<a name='{gen_anchor(txt)}'></a>"


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


def italicize(txt: str):
    """
    Italicize.

    :param txt: A string object.
    :return: Italicized string markdown syntax.
    """
    return "\n*" + " ".join(txt.replace("\n", "").split()) + "*\n"


def add_python_snippet(txt: str, expandable: bool = True):
    """
    Add a python snippet.

    :param txt: A string object.
    :param expandable: If true, puts code in <details></details> syntax.
    :return: Python string markdown syntax.
    """
    md_str = f"\n```python\n{txt}\n```"

    if expandable:
        md_str = f"\n<details>\n<summary>source code</summary>\n{md_str}\n</details>\n"

    return md_str


def add_table(df: pd.DataFrame) -> str:
    """
    Add table.

    :param df: A pandas dataframe.
    :return: Table markdown syntax.
    """
    return tabulate(df, tablefmt="pipe", headers="keys", showindex=False)


def add_index(headers: List[str], indent: int = 0) -> str:
    """
    Add index.

    :param headers: A list of header strings.
    :param indent: The indentation level for the link.
    :return: Markdown syntax for an index.
    """
    backslash = "\_"
    return list_to_md([f"[{re.sub('_', backslash, h)}](#{gen_anchor(h)})" for h in headers], indent=indent)
