# a
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime("%s")}.py'
with open(TAPE, 'w') as f:
    f.write("""
# b
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
with open(TAPE, 'r') as f:
    program = f.read()
with open(TAPE, 'w') as f:
    f.write(\"\"\"# a
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\\\"%s\\\")}.py'
with open(TAPE, 'w') as f:
    f.write(\\\"\\\"\\\"\"\"\"+str(program.replace('\\\\','\\\\\\\\').replace('\"','\\\\\"'))+\"\"\"\\\"\\\"\\\")
\"\"\" + program)""")

# b
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime("%s")}.py'
with open(TAPE, 'r') as f:
    program = f.read()
with open(TAPE, 'w') as f:
    f.write("""# a
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
with open(TAPE, 'w') as f:
    f.write(\"\"\""""+str(program.replace('\\','\\\\').replace('"','\\"'))+"""\"\"\")
""" + program)