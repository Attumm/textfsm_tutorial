"""
STEP 2: Using States - Parsing Data After a Separator Line

Learning Objective:
This step introduces the concept of states in TextFSM. We will learn
how to use states to ignore lines until a specific marker line is found,
and then start parsing data only after that marker.

In this example, we want to parse names that appear *after* a separator line
"------------------".

How to run:
python basics/step_2_states_separator.py
"""

from common import run_textfsm
from pprint import pprint

# 1. Define the TextFSM template with states
#    - We have two states: 'Start' and 'Names'
#    - Initially, we are in the 'Start' state.
#    - In 'Start' state, we look for the separator line "------------------".
#    - When we find the separator, we transition to the 'Names' state.
#    - In the 'Names' state, we parse the lines with names.
template = """
Value FirstName ([\w]+)
Value LastName ([\w]+)

Start
  ^------------------ -> Names
  ^.*

Names
  ^${FirstName} ${LastName} -> Record
""".strip()

# 2. Example data with header, separator, and names
output = """
Firstname Lastname
------------------
John Doe
Jane Dye
""".strip()

expected_result = [
    {'FirstName': 'John', 'LastName': 'Doe'},
    {'FirstName': 'Jane', 'LastName': 'Dye'}
]

if __name__ == '__main__':
    result = run_textfsm(output, template)
    assert result == expected_result
    print("Parsed Data (List of Dictionaries):")
    pprint(result)