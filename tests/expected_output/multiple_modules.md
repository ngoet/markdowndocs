# <a name='codedocumentation'></a>Code documentation

* [test\_cases/class\_and\_functions](#testcasesclassandfunctions)


	* [Greetings](#greetings)


		* [Greetings.\_\_init\_\_](#greetingsinit)


		* [Greetings.ask\_name](#greetingsaskname)


		* [Greetings.greet](#greetingsgreet)


* [test\_cases/one\_function](#testcasesonefunction)


	* [greet](#greet)


* [test\_cases/multiple\_functions](#testcasesmultiplefunctions)


	* [ask\_name](#askname)


	* [greet](#greet)

## <a name='testcasesclassandfunctions'></a>test\_cases/class\_and\_functions
&uparrow; Back to [code documentation index](#codedocumentation)

### <a name='classes'></a>Classes

* [Greetings](#greetings)

#### <a name='greetings'></a>Greetings
Very friendly class that greets people.
##### <a name='functions'></a>Functions

* [Greetings.\_\_init\_\_](#greetingsinit)

* [Greetings.ask\_name](#greetingsaskname)

* [Greetings.greet](#greetingsgreet)

###### <a name='greetingsinit'></a>Greetings.\_\_init\_\_
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_functions)

&uparrow; Back to [class index](#Greetings)

*No docstrings available.*
<details>
<summary>source code</summary>

```python
    def __init__(self, name):
        self.name = name

```
</details>

###### <a name='greetingsaskname'></a>Greetings.ask\_name
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_functions)

&uparrow; Back to [class index](#Greetings)


        Ask name.

        :return: A question.

<details>
<summary>source code</summary>

```python
    def ask_name(self) -> str:
        """
        Ask name.

        :return: A question.
        """
        return f"What's your {self.name}?"

```
</details>

###### <a name='greetingsgreet'></a>Greetings.greet
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_functions)

&uparrow; Back to [class index](#Greetings)


        Generates a greeting.

        :return: A greeting.

<details>
<summary>source code</summary>

```python
    def greet(self) -> str:
        """
        Generates a greeting.

        :return: A greeting.
        """
        return f"Hello {self.name}"

```
</details>

## <a name='testcasesonefunction'></a>test\_cases/one\_function
&uparrow; Back to [code documentation index](#codedocumentation)

### <a name='functions'></a>Functions

* [greet](#greet)

#### <a name='greet'></a>greet
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/one_function)


    Generates a greeting.

    :param name: A name.
    :return: A greeting.

<details>
<summary>source code</summary>

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
<summary>source code</summary>

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
<summary>source code</summary>

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
