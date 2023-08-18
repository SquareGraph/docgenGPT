
# DocgenGPT 0.2.0

A handy way to autmatically create docstrings and markdowns

## Overview

The provided code consists of three main classes:

- `AutoDoc`: A class that automates the generation of docstrings for Python files.
- `PyFile`: A dataclass that represents Python files, with methods to format answers and initialize some of its attributes.
- `SystemMessage`: An enumeration that defines three types of system messages.

## Example Usage

Quick look how it works. The output of the AutoDoc.generate_docstrings() is a directory with a new version of files. 
It will be placed in the same root path as provided.

```python
# Define the path to the directory containing Python files and the context
path_dir = Path("/path/to/directory")
context = {
    "filename1": "This is the context for filename1.py",
    "filename2": "This is the context for filename2.py",
    # ... add context for other files as needed
}

# Initialize the AutoDoc class
autodoc = AutoDoc(path_dir=path_dir, openai_api_key="YOUR_OPENAI_API_KEY", context=context)

# Generate docstrings for the Python files
autodoc.generate_docstrings()
```

## Class Descriptions

### AutoDoc

Attributes:

- `raw_paths`: Paths to Python files.
- `documents`: Loaded Python documents.
- `pyfiles`: A list of `PyFile` instances.
- `llm`: Instance of the ChatOpenAI model.
- `vectorstore`: Instance of Chroma with embedded documents.

Methods:

- `__get_python_paths(path_dir: Path)`: Retrieves paths to Python files from a given directory.
- `__get_pyfiles(context: Dict)`: Generates a list of `PyFile` instances from documents.
- `retrive_docs(pyfile: PyFile)`: Retrieves docs for a given `PyFile` instance.
- `__get_docstrings()`: Gathers docstrings for the Python files.
- `generate_docstrings()`: Generates docstrings and writes them to Python files in a new directory.


### PyFile

Attributes:

- `path`: Path to the file.
- `context`: The context of the file.
- `page_content`: Content of the page.
- `answer`: (Optional) Answer to a given query.

Methods:

- `from_document(document: Document, context: str)`: A class method that creates an instance of `PyFile` from a document and context.
- `format_answer()`: A method that formats the answer, taking into account code blocks.
- `__post_init__()`: A post-initialization method that sets the name attribute of the instance based on the file path.

### SystemMessage

This is an `Enum` class that defines three types of messages:

1. `open`: A message to act as a senior programmer with vast Python knowledge.
2. `docs`: A request to create docstrings and type hints for the provided code.
3. `markdown`: A request to create a markdown file that describes the provided code.

#### Known issues in 0.2.0

- Sometimes struggling with retrieval from vectorstore in longer context


#### Scheduled work
- Testing different databases
- Adding function to create docstrings not in a QAretrieval way
- Adding markdown generation
