#Importing Necessary Libraries

import os
from collections import Counter
import pyfiglet
import termtables as tt


title = pyfiglet.figlet_format("LR (0) Parsing", font="digital")
print(title)

def addDot(dot):
    addDotVar = dot.replace("->", "->.")
    return addDotVar

def compressedName(name: str):
    compResult = Counter(name)
    comp = ''
    for r in compResult:
        comp += r + str(compResult[r])
    return comp

#Function to Save file
def saveFile(final_string, grammar, name):
    directory = os.path.dirname("stringParsing/" + str(grammar) + "/")
    if not os.path.exists(directory):
        print("Creating this Director......")
        os.makedirs(directory)

    with open("stringParsing/{0}/{1}.txt".format(grammar, name), 'w') as fileParsing:
        fileParsing.write(final_string)

