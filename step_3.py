import textfsm
from io import StringIO


template = """
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start
  ^------------------ -> Names

Names
  ^${Firstname}.${Lastname} -> Record
""".strip()

#This will match Firstname and Lastname
#We would only like to match after the seperation line
template = """
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start
  ^${Firstname}.${Lastname} -> Record
""".strip()

result = """
Firstname Lastname
------------------
John Doe
Jane Dye
"""

def run(result):
    t = textfsm.TextFSM(StringIO(template))
    raw_list = t.ParseText(result.strip())
    return [dict(zip(t.header, i)) for i in raw_list]

print(run(result))

