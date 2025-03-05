"""
STEP 3_2: Value List - Collecting Multiple Matches into a List

Learning Objective:
This step demonstrates the 'Value List' option in TextFSM.
'Value List' allows you to collect all matches for a particular Value
within a single record into a list.

How to run:
python basics/step_3_2_value_list.py
"""

from common import run_textfsm
from pprint import pprint

template = """
Value FirstName ([\\w]+)
Value LastNames List ([\\w]+)

Start
  ^${FirstName} ${LastNames} -> Record
""".strip()

output = """
John Doe
Sara May
Katy Brown Wilson
""".strip()

expected_result = [
    {'FirstName': 'John', 'LastNames': ['Doe']},
    {'FirstName': 'Sara', 'LastNames': ['May']},
    {'FirstName': 'Katy', 'LastNames': ['Brown', 'Wilson']}
]

if __name__ == '__main__':
    result = run_textfsm(output, template)
    assert result == expected_result, f"Expected {expected_result}, got {result}"
    print("Parsed Data (List of Dictionaries):")
    pprint(result)
