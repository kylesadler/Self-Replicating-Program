# Part A: store Part B's code
tape = """
# Part B: use Part A's output to rerwite the program that is currently running
print(\"\"\"# Part A: store Part B's code
tape = \\\"\\\"\\\"\"\"\"+str(tape.replace('\\\\','\\\\\\\\').replace('\"','\\\\\"'))+\"\"\"\\\"\\\"\\\"
\"\"\" + tape)"""

# Part B: use Part A's output to rerwite the program that is currently running
print("""# Part A: store Part B's code
tape = \"\"\""""+str(tape.replace('\\','\\\\').replace('"','\\"'))+"""\"\"\"
""" + tape)
