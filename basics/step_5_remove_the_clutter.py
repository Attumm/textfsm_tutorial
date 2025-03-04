"""
STEP 5: Remove the Clutter (Without Skipping 'other users')

Learning Objective:
In this step, we show how to skip or handle clutter (headers, dashes, etc.)
while preserving specific lines (like "other users") using TextFSM states.
We do not skip "other users"; we simply acknowledge the line before continuing
to capture valid records.

How to run:
python basics/step_5_remove_the_clutter.py
"""

from common import run_textfsm
from pprint import pprint

# 1. Define the TextFSM template:
#    - We skip the dashed line in 'Start' and transition to state 'Name'.
#    - In 'Name' state, we "match" (but do not record) the line "other users",
#      then capture names that match the Firstname/Lastname pattern.

template = r"""
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start
  ^------------------ -> Name

Name
  ^other users
  ^${Firstname}\s+${Lastname} -> Record
""".strip()

# 2. Example data: includes headers, dashed lines, a line "other users",
#    and the actual names we want to capture.
output = """
Firstname Lastname
------------------
John Doe
Jane Dye

other users

Jon Dotwo
Jan Dytwo
""".strip()

# 3. We expect to parse all valid Firstname/Lastname lines,
#    while "other users" is *not* removed or skipped. It simply doesn't produce a record.
expected_result = [
    {"Firstname": "John", "Lastname": "Doe"},
    {"Firstname": "Jane", "Lastname": "Dye"},
    {"Firstname": "Jon",  "Lastname": "Dotwo"},
    {"Firstname": "Jan",  "Lastname": "Dytwo"}
]

if __name__ == '__main__':
    result = run_textfsm(output, template)
    assert result == expected_result, "The parsed result does not match the expected output."
    print("Parsed Data (List of Dictionaries):")
    pprint(result)
