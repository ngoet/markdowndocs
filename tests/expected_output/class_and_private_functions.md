# <a name='codedocumentation'></a>Code documentation

* [test\_cases/class\_and\_private\_functions](#testcasesclassandprivatefunctions)


	* [Greetings](#greetings)


		* [Greetings.\_\_init\_\_](#greetingsinit)


		* [Greetings.\_\_ask\_name](#greetingsaskname)


		* [Greetings.\_greet](#greetingsgreet)

## <a name='testcasesclassandprivatefunctions'></a>test\_cases/class\_and\_private\_functions
&uparrow; Back to [code documentation index](#codedocumentation)

### <a name='classes'></a>Classes

* [Greetings](#greetings)

#### <a name='greetings'></a>Greetings
Very friendly class that greets people.
##### <a name='functions'></a>Functions

* [Greetings.\_\_init\_\_](#greetingsinit)

* [Greetings.\_\_ask\_name](#greetingsaskname)

* [Greetings.\_greet](#greetingsgreet)

###### <a name='greetingsinit'></a>Greetings.\_\_init\_\_
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_private_functions)

&uparrow; Back to [class index](#Greetings)

*No docstrings available.*
<details>
<summary>raw code</summary>

```python
    def __init__(self, name):
        self.name = name

```
</details>

###### <a name='greetingsaskname'></a>Greetings.\_\_ask\_name
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_private_functions)

&uparrow; Back to [class index](#Greetings)


        Ask name.

        :return: A question.

<details>
<summary>raw code</summary>

```python
    def __ask_name(self) -> str:
        """
        Ask name.

        :return: A question.
        """
        return f"What's your {self.name}?"

```
</details>

###### <a name='greetingsgreet'></a>Greetings.\_greet
&uparrow; Back to [code documentation index](#codedocumentation)

&uparrow; Back to [module index](#test_cases/class_and_private_functions)

&uparrow; Back to [class index](#Greetings)


        Generates a greeting.

        :return: A greeting.

<details>
<summary>raw code</summary>

```python
    def _greet(self) -> str:
        """
        Generates a greeting.

        :return: A greeting.
        """
        return f"Hello {self.name}"

```
</details>
