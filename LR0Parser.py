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

#Function to find closure
def findClosure(gram):
    flag = [gram]
    for i in flag:
        j = i[i.index(".") + 1]
        if j != len(i) - 1:
            for k in prod:
                if k[0][0] == j and (append_dot(k)) not in flag:
                    flag.append(append_dot(k))
        else:
            for k in prod:
                if k[0][0] == j and i not in flag:
                    flag.append(i)

    return flag