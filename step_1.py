import textfsm
from io import StringIO


template = """
Value FirstName ([\w]+)
Value LastName ([\w]+)

Start
  ^${FirstName}.${LastName}
""".strip()

result = """
John Doe
"""

def run(result):
    t = textfsm.TextFSM(StringIO(template))
    raw_list = t.ParseText(result.strip())
    return [dict(zip(t.header, i)) for i in raw_list]

print(run(result))

