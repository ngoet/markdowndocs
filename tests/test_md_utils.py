import unittest
import pandas as pd
from markdowndocs import md_utils


class TestMdUtils(unittest.TestCase):
    """
    Test cases for the markdown utility functions.
    """

    def test_list_to_md(self) -> None:
        """
        Test the conversion of a list to markdown format.

        This test verifies that a list of items is correctly converted to markdown format.
        """
        self.assertEqual(md_utils.list_to_md(["item1", "item2", "item3"]), "\n\n* item1\n\n* item2\n\n* item3\n")

    def test_italicize(self) -> None:
        """
        Test the italicization of text.

        This test verifies that text is correctly italicized using markdown syntax.
        """
        self.assertEqual(md_utils.italicize("text"), "\n*text*\n")

    def test_add_python_snippet(self) -> None:
        """
        Test the addition of a Python snippet.

        This test verifies that a Python snippet is correctly formatted and wrapped in markdown syntax.
        """
        self.assertEqual(
            md_utils.add_python_snippet('print("Hello, World!")'),
            '\n<details>\n<summary>source code</summary>\n\n```python\nprint("Hello, World!")\n```\n</details>\n',
        )

    def test_add_table(self) -> None:
        """
        Test the addition of a table.

        This test verifies that a pandas DataFrame is correctly converted to a markdown table.
        """
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        self.assertEqual(
            md_utils.add_table(df),
            "|   col1 |   col2 |\n|-------:|-------:|\n|      1 |      4 |\n|      2 |      5 |\n|      3 |      6 |",
        )

    def test_add_index(self) -> None:
        """
        Test the addition of an index.

        This test verifies that a list of headers is correctly formatted as an index in markdown syntax.
        """
        self.assertEqual(
            md_utils.add_index(["header1", "header2"]), "\n\n* [header1](#header1)\n\n* [header2](#header2)\n"
        )


if __name__ == "__main__":
    unittest.main()
