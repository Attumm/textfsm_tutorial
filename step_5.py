import textfsm
import json
from io import StringIO
### step 5 remove the clutter
# In this step we will have to remove the clutter.
# Learn about states they really powerfull tool 
##
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

other users
 
Jon Dotwo
Jan Dytwo
"""

def run(result):
    t = textfsm.TextFSM(StringIO(template))
    raw_list = t.ParseText(result.strip())
    return [dict(zip(t.header, i)) for i in raw_list]

output = run(result)

print(json.dumps(output, indent=2))


template_with_answer = """
Value Firstname ([\w]+)
Value Lastname ([\w]+)

Start
  ^------------------ -> Name

Name
  ^other users  
  ^${Firstname}.${Lastname} -> Record

""".strip()
