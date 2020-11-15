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
    f.write(\"\"\"
# a
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\\\"%s\\\")}.py'
with open(TAPE, 'w') as f:
    f.write(\\\"\\\"\\\"\"\"\"+str(program)+\"\"\"\\\"\\\"\\\")
\"\"\" + program)
""")

# b
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime("%s")}.py'
with open(TAPE, 'r') as f:
    program = f.read()
with open(TAPE, 'w') as f:
    f.write("""
# a
from datetime import datetime
TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
with open(TAPE, 'w') as f:
    f.write(\"\"\""""+str(program)+"""\"\"\")
""" + program)









# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime("%s")}.py'

# # a
# with open(TAPE, 'w') as f:
#     f.write("""
# # b
# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime("%s")}.py'
# with open(TAPE, 'r') as f:
#     program = f.read()

# with open(TAPE, 'w') as f:
#     f.write(\"\"\"
# with open(TAPE, 'w') as f:
#     f.write(\\\"\\\"\\\"
# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime(\\\"%s\\\")}.py'
# with open(TAPE, 'w') as f:
#     f.write(\"\"\"+str(program)+\"\"\")
# \\\"\\\"\\\")
# \"\"\" + program)
# """)

# # b
# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime("%s")}.py'
# with open(TAPE, 'r') as f:
#     program = f.read()
# with open(TAPE, 'w') as f:
#     f.write("""
# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime(\"%s\")}.py'
# with open(TAPE, 'w') as f:
#     f.write(\"\"\"
# from datetime import datetime
# TAPE = f'replicator{datetime.now().strftime(\\\"%s\\\")}.py'
# with open(TAPE, 'w') as f:
#     f.write("""+str(program)+""")
# \"\"\")
# """ + program)