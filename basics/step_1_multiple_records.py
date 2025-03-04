"""
STEP 1: Parsing Multiple Records - Multiple Lines of Data

Learning Objective:
This step demonstrates how TextFSM parses multiple lines of input data.
When the template matches a line and the 'Record' action is used, TextFSM
creates a record. If there are multiple matching lines in the input, TextFSM
will create multiple records.

How to run:
python basics/step_1_multiple_records.py
"""

import textfsm
from io import StringIO
from pprint import pprint

# 1. Define the TextFSM template (SPACE separated names)
template = """
Value FirstName ([\w]+)
Value LastName ([\w]+)

Start
  ^${FirstName} ${LastName} -> Record
""".strip()

# 2. Example data with TWO names (two lines)
output = """
John Doe
Jane Dye
""".strip()

expected_result = [
    {'FirstName': 'John', 'LastName': 'Doe'},
    {'FirstName': 'Jane', 'LastName': 'Dye'}
]

if __name__ == '__main__':
    # Create TextFSM object and parse
    tfsm = textfsm.TextFSM(StringIO(template))
    raw_list = tfsm.ParseText(output)
    result = [dict(zip(tfsm.header, i)) for i in raw_list]

    assert result == expected_result
    print("Parsed Data (List of Dictionaries):")
    pprint(result)
