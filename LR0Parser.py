#Importing Necessary Libraries

import os
from collections import Counter
import pyfiglet
import termtables as tt

def addDot(dot):
    addDotVar = dot.replace("->", "->.")
    return addDotVar

def compressedName(name: str):
    compResult = Counter(name)
    comp = ''
    for r in compResult:
        comp += r + str(compResult[r])
    return comp