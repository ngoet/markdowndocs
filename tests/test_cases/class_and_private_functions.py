class Greetings:
    """Very friendly class that greets people."""

    def __init__(self, name):
        self.name = name

    def _greet(self) -> str:
        """
        Generates a greeting.

        :return: A greeting.
        """
        return f"Hello {self.name}"

    def __ask_name(self) -> str:
        """
        Ask name.

        :return: A question.
        """
        return f"What's your {self.name}?"
