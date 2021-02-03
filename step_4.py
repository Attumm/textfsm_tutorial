import textfsm
from io import StringIO


#Common Problems Error messages and meanings


# The newline under "Start" will create the following error: 
# textfsm.TextFSMTemplateError: Invalid state name: '  ^${Firstname}.${Lastname} -> Record'. Line: 6
template = """
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start

  ^${Firstname}.${Lastname} -> Record
""".strip()

# The "${Firstname}" has a Typo 
# textfsm.TextFSMTemplateError: Duplicate or invalid variable substitution: '^${FirstName}.${Lastname}'. Line: 5.
template = """
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start
  ^${FirstName}.${Lastname} -> Record
""".strip()

result = """
John Doe
Jane Dye
"""

def run(result):
    t = textfsm.TextFSM(StringIO(template))
    raw_list = t.ParseText(result.strip())
    return [dict(zip(t.header, i)) for i in raw_list]

print(run(result))

