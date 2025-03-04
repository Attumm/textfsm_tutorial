"""
STEP 3_1: Value Required - Ensuring Value Match for Valid Records

Learning Objective:
This step demonstrates the 'Value Required' option in TextFSM.
'Value Required' ensures that a record is only created if a Value marked
as 'Required' is successfully matched in the input line.

In this example, we want to parse names, but we want to ensure that both
'FirstName' and 'LastName' are present for a valid record. We will mark
'LastName' as a 'Required' Value.

How to run:
python basics/step_3_1_value_required.py
"""

from common import run_textfsm
from pprint import pprint

# 1. Define the TextFSM template
#    - Use 'Value Required LastName' so that if LastName is not matched, the record is not appended.
template = """
Value FirstName ([\\w]+)
Value Required LastName ([\\w]+)

Start
  ^${FirstName}\\s+${LastName} -> Record
""".strip()

# 2. Example data with some lines missing LastNames
output = """
John Doe
Jane
Peter Pan
""".strip()

expected_result = [
    {'FirstName': 'John', 'LastName': 'Doe'},
    {'FirstName': 'Peter', 'LastName': 'Pan'}  # "Jane" is skipped, LastName missing
]

if __name__ == '__main__':
    result = run_textfsm(output, template)
    print("Result:", result)
    assert result == expected_result, "The parsed result does not match the expected output."
    print("Parsed Data (List of Dictionaries):")
    pprint(result)
