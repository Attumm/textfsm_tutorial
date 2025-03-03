"""
STEP 3_0: Value Filldown - Persisting Value to Subsequent Records

Learning Objective:
This step demonstrates the 'Value Filldown' option in TextFSM.
'Value Filldown' allows a captured Value to persist and be associated
with subsequent records until a new value is matched for the same Value.

In this example, we will parse names grouped under categories (e.g., Group A, Group B).
'Value Filldown Group' will ensure that all names following a 'Group' line
are associated with that Group until the next 'Group' line appears.

How to run:
python basics/step_3_0_value_filldown.py
"""

from common import run_textfsm
from pprint import pprint

# 1. Define the TextFSM template with Value Filldown
#    - 'Value Filldown Group (Group\s\w+)' defines 'Group' as a Filldown Value.
#    - Once 'Group' is matched, its value persists for following records
#      until a new 'Group' line is encountered.
template = """
Value Filldown Group (Group\s\w+)
Value FirstName (\w+)
Value LastName (\w+)

Start
  ^${Group} -> Start
  ^${FirstName}\s+${LastName} -> Record
""".strip()

# 2. Example data with groups and names
output = """
Group A
John Doe
Jane Dye
Group B
Peter Pan
""".strip()

expected_result = [
    {'Group': 'Group A', 'FirstName': 'John', 'LastName': 'Doe'},
    {'Group': 'Group A', 'FirstName': 'Jane', 'LastName': 'Dye'},
    {'Group': 'Group B', 'FirstName': 'Peter', 'LastName': 'Pan'},
    {'Group': 'Group B', 'FirstName': '', 'LastName': ''},
]

if __name__ == '__main__':
    result = run_textfsm(output, template)
    assert result == expected_result

    print("Parsed Data (List of Dictionaries):")
    pprint(result)