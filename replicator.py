# Part A: write Part B's code to a new file
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime("%s")}.py'
with open(TAPE, 'w') as f:
    f.write("""
# Part B: use Part A's output to rerwite the program that is currently running
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
with open(TAPE, 'r') as f:
    program = f.read()
with open(TAPE, 'w') as f:
    f.write(\"\"\"# Part A: write Part B's code to a new file
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\\\"%s\\\")}.py'
with open(TAPE, 'w') as f:
    f.write(\\\"\\\"\\\"\"\"\"+str(program.replace('\\\\','\\\\\\\\').replace('\"','\\\\\"'))+\"\"\"\\\"\\\"\\\")
\"\"\" + program)""")

# Part B: use Part A's output to rerwite the program that is currently running
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime("%s")}.py'
with open(TAPE, 'r') as f:
    program = f.read()
with open(TAPE, 'w') as f:
    f.write("""# Part A: write Part B's code to a new file
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
with open(TAPE, 'w') as f:
    f.write(\"\"\""""+str(program.replace('\\','\\\\').replace('"','\\"'))+"""\"\"\")
""" + program)