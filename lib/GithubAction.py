
from os import environ

def setOutput(name, value):
    output_file = environ.get("GITHUB_OUTPUT")
    with open(output_file, "w") as output:
        output.write(name + "=" + value + "\n")
