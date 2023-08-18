"""CLI interface for AutoDoc"""
from pathlib import Path
from .autodoc import AutoDoc

__all__ = ["AutoDocWizard"]


class AutoDocWizard:
    """CLI wizard for AutoDoc class."""

    def __init__(self):
        pass

    def get_path_dir(self) -> Path:
        """
        Prompts the user to enter the path to the directory containing Python files.

        Returns:
            Path: The path to the directory containing Python files.
        """
        return Path(
            input("Please enter the path to the directory containing Python files: ")
        )

    def get_openai_api_key(self) -> str:
        """
        Prompts the user to enter their OpenAI API key.

        Returns:
            str: The OpenAI API key.
        """
        return input("Please enter your OpenAI API key: ")

    def get_context(self, path: Path) -> dict:
        """
        Prompts the user to specify the context for each Python file in the given directory.

        Args:
            path (Path): The path to the directory containing Python files.

        Returns:
            dict: A dictionary mapping each Python file name to its corresponding context.
        """
        filenames = [
            file.name.split(".")[0] for file in path.iterdir() if file.suffix == ".py"
        ]
        context = {}
        print("Now, let's specify the context for each Python file.")
        for filename in filenames:
            file_context = input(f"Enter the context for {filename}: ")
            context[filename] = file_context
        return context

    def get_model_name(self) -> str:
        """
        Prompts the user to enter the name of the OpenAI model to use.

        Returns:
            str: The name of the OpenAI model.
        """
        return (
            input(
                "Please enter the name of the OpenAI model to use (default is 'gpt-3.5-turbo'): "
            )
            or "gpt-3.5-turbo"
        )

    def get_temperature(self) -> int:
        """
        Prompts the user to enter the temperature setting for the OpenAI model.

        Returns:
            int: The temperature setting for the OpenAI model.
        """
        temp = input(
            "Please enter the temperature setting for the OpenAI model (default is 0): "
        )
        return int(temp) if temp else 0

    def run(self) -> None:
        """
        Runs the AutoDoc wizard.

        This method prompts the user for various inputs, creates an instance of the AutoDoc class,
        and generates docstrings using the provided inputs.
        """
        path_dir = self.get_path_dir()
        openai_api_key = self.get_openai_api_key()
        context = self.get_context(path_dir)
        model_name = self.get_model_name()
        temperature = self.get_temperature()

        autodoc = AutoDoc(
            path_dir=path_dir,
            openai_api_key=openai_api_key,
            context=context,
            model_name=model_name,
            temperature=temperature,
        )
        autodoc.generate_docstrings()
        print("Docstrings generated successfully!")
