import os
import unittest
from dataclasses import dataclass
from typing import List, Optional

from markdowndocs.cli import main, set_up_parser

full_path = os.path.join
os.chdir(os.path.dirname(os.path.realpath(__file__)))

tmpdir = "tmp"
if not os.path.exists(tmpdir):
    os.makedirs(tmpdir)


@dataclass
class Scenario:
    input_modules: List[str]
    output_file_name: str


markdowndocs_scenarios = [
    Scenario(input_modules=[full_path("test_cases", "one_function")], output_file_name="one_function"),
    Scenario(input_modules=[full_path("test_cases", "class_and_functions")], output_file_name="class_and_functions"),
    Scenario(input_modules=[full_path("test_cases", "multiple_functions")], output_file_name="multiple_functions"),
    Scenario(
        input_modules=[
            full_path("test_cases", "one_function"),
            full_path("test_cases", "class_and_functions"),
            full_path("test_cases", "multiple_functions"),
        ],
        output_file_name="multiple_modules",
    ),
    Scenario(
        input_modules=[full_path("test_cases", "class_and_private_functions")],
        output_file_name="class_and_private_functions",
    ),
]


@dataclass
class MddocsOptionScenario:
    input_modules: List[str]
    output_file_name: str
    option: str
    should_include: Optional[str] = None
    should_not_include: Optional[str] = None


mddocs_options_scenarios = [
    MddocsOptionScenario(
        input_modules=[full_path("test_cases", "one_function")],
        output_file_name="one_function_option",
        option="--exclude-code",
        should_not_include="<summary>raw code</summary>",
    ),
    MddocsOptionScenario(
        input_modules=[full_path("test_cases", "function_with_import_statements")],
        output_file_name="function_with_import_statements_option",
        option="--exclude-dependencies",
        should_not_include="<a name='dependencies'></a>Dependencies",
    ),
]


class TestMarkdownDocs(unittest.TestCase):
    """
    Test functions for markdowndocs.

    Produces .md documentation and compares against pre-defined, expected outputs.
    """

    def test_markdowndocs_scenarios(self) -> None:
        """
        Test markdowndocs markdowndocs_scenarios.

        Generates markdowndocs .md output and validates against pre-defined output.
        """

        self.parser = set_up_parser()
        for scenario in markdowndocs_scenarios:
            parsed = self.parser.parse_args([f"-m{scenario.input_modules[0]}"])
            parsed.module_names += scenario.input_modules[1:]
            file_path = os.path.join("tmp", scenario.output_file_name)
            parsed.output_file_name = file_path
            main(parsed)
            with open(file_path + ".md", "r") as output:
                output_md = output.read()
            with open(os.path.join("expected_output", scenario.output_file_name + ".md")) as expected_output:
                expected_output_md = expected_output.read()

            assert (
                output_md == expected_output_md
            ), f"Result for scenario {scenario.output_file_name} does not match expected output."
            output.close()
            expected_output.close()

    def test_mddocs_options(self) -> None:
        """
        Test mddocs options.

        Verifies that specific .md syntax is / is not present in output when different arguments are used.
        """
        self.parser = set_up_parser()
        for scenario in mddocs_options_scenarios:
            parsed = self.parser.parse_args([f"-m{scenario.input_modules[0]}", scenario.option])
            parsed.module_names += scenario.input_modules[1:]
            file_path = os.path.join("tmp", scenario.output_file_name)
            parsed.output_file_name = file_path
            main(parsed)
            with open(file_path + ".md", "r") as output:
                output_md = output.read()

            if scenario.should_not_include:
                assert scenario.should_not_include not in output_md, (
                    f"Scenario {scenario.output_file_name}: {scenario.should_not_include} should NOT be present in  "
                    f"the output when the {scenario.option} argument is used."
                )

            if scenario.should_include:
                assert scenario.should_include in output_md, (
                    f"Scenario {scenario.output_file_name}: {scenario.should_include} SHOULD be present in the output"
                    f"when the {scenario.option} argument is used."
                )

                output.close()


if __name__ == "__main__":
    unittest.main()
