# <a name='codedocumentation'></a>Code documentation

* [test\_cases/multiple\_functions](#testcasesmultiplefunctions)


	* [ask\_name](#askname)


	* [greet](#greet)

## <a name='testcasesmultiplefunctions'></a>test\_cases/multiple\_functions
&uparrow; Back to [code documentation index](#codedocumentation)

### <a name='functions'></a>Functions

* [ask\_name](#askname)

* [greet](#greet)

#### <a name='askname'></a>ask\_name
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/multiple_functions)


    Ask name.

    :param name: A name.
    :return: A question.

<details>
<summary>raw code</summary>

```python
def ask_name(name: str) -> str:
    """
    Ask name.

    :param name: A name.
    :return: A question.
    """
    return f"What's your {name}?"

```
</details>

#### <a name='greet'></a>greet
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/multiple_functions)


    Generates a greeting.

    :param name: A name.
    :return: A greeting.

<details>
<summary>raw code</summary>

```python
def greet(name: str) -> str:
    """
    Generates a greeting.

    :param name: A name.
    :return: A greeting.
    """
    return f"Hello {name}"

```
</details>
