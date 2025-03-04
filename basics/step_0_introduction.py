"""
STEP 0: Introduction to TextFSM - Parsing a Simple Name

Learning Objective:
This is a very first introduction to TextFSM. We will learn to parse
a simple name like "John Doe" and extract the first and last name
using a TextFSM template defined directly in the Python code.

TextFSM is a Python library for parsing unstructured text data based on templates.
It's great for network device outputs, logs, and other text formats that don't
have a consistent structure.

How to run:
python basics/step_0_introduction.py
"""

from common import run_textfsm

# 1. Define the TextFSM template as a string
#    - 'Value FirstName ([\w]+)' defines a Value named 'FirstName'
#      that will capture one or more word characters (letters, numbers, underscore).
#    - 'Value LastName ([\w]+)' does the same for 'LastName'.
#    - 'Start' state is the initial state of the template.
#    - '^${FirstName} ${LastName}' is a regular expression that matches
#      the beginning of a line ('^') followed by the 'FirstName' Value,
#      a space (' '), and the 'LastName' Value.
template = """
Value FirstName ([\w]+)
Value LastName ([\w]+)

Start
  ^${FirstName}.${LastName}
""".strip()  # .strip() removes leading/trailing whitespace

output = """
John Doe
"""

expected_result = [{'FirstName': 'John', 'LastName': 'Doe'}]
# --- Expected Output ---
# Parsed Data (List of Dictionaries):
# [{'FirstName': 'John', 'LastName': 'Doe'}]
if __name__ == '__main__':
    result = run_textfsm(output, template)
    assert result == expected_result
    print(result)
