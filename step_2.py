import textfsm
from io import StringIO


# If there are two items, Record will match the line again
template = """
Value FirstName ([\w]+)
Value LastName ([\w]+)

Start
  ^${FirstName}.${LastName} -> Record
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

