#---------------- Importing Necessary Libraries ----------------

import os
import time
from collections import Counter
import pyfiglet
import termtables as tt

#----------------Done Importing Necessary Libraries ----------------

title = pyfiglet.figlet_format("LR (0) Parsing", font="digital")
print(title)

#----------------Defining Important Functions ----------------
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
            for k in productionRules:
                if k[0][0] == j and (addDot(k)) not in flag:
                    flag.append(addDot(k))
        else:
            for k in productionRules:
                if k[0][0] == j and i not in flag:
                    flag.append(i)

    return flag

#Fucntion to Swap Values
def swapValues(newValue, posValue):
    newValue = list(newValue)
    temp = newValue[posValue]
    if posValue != len(newValue):
        newValue[posValue] = newValue[posValue + 1]
        newValue[posValue + 1] = temp
        newFinal = "".join(newValue)
        return newFinal
    else:
        return "".join(newValue)

#go to function
def gotoFucntion(var1):
    arr = []
    pos = var1.index(".")
    if pos != len(var1) - 1:
        j = list(var1)
        k = swapValues(j, pos)
        if k.index(".") != len(k) - 1:
            l = findClosure(k)
            return l
        else:
            arr.append(k)
            return arr
    else:
        return var1

def Terminals(inputTerminal):
    terminalSet = set()
    for p in inputTerminal:
        x1 = p.split('->')
        for t in x1[1].strip():
            if not t.isupper() and t != '.' and t != '':
                terminalSet.add(t)

    terminalSet.add('$')

    return terminalSet

#function to store non terminals
def nonTerminals(gram):
    terms = set()
    for p in gram:
        x1 = p.split('->')
        for t in x1[1].strip():
            if t.isupper():
                terms.add(t)
    return terms

def getList(graph, state):
    finalList = []
    for g in graph:
        if int(g.split()[0]) == state:
            finalList.append(g)

    return finalList

#----------------Done Defining Important Functions ----------------


productionRules = []
itemSet = []
flag = []

with open("input.txt", 'r') as fp:
    for i in fp.readlines():
        productionRules.append(i.strip())

productionRules.insert(0, "X->.S")
print("---------------------------------------------------------------")
print("Augmented Grammar")
print(productionRules)

productionNum = {}
for i in range(1, len(productionRules)):
    productionNum[str(productionRules[i])] = i

appendingClosure = findClosure("X->.S")
itemSet.append(appendingClosure)

stateNumbers = {}
dfaRules = {}
numberofItems = 0

while True:
    if len(itemSet) == 0:
        break

    jk = itemSet.pop(0)
    kl = jk
    flag.append(jk)
    stateNumbers[str(jk)] = numberofItems
    numberofItems += 1

    if len(jk) > 1:
        for item in jk:
            jl = gotoFucntion(item)
            if jl not in itemSet and jl != kl:
                itemSet.append(jl)
                dfaRules[str(stateNumbers[str(jk)]) + " " + str(item)] = jl
            else:
                dfaRules[str(stateNumbers[str(jk)]) + " " + str(item)] = jl

for item in flag:
    for j in range(len(item)):
        if gotoFucntion(item[j]) not in flag:
            if item[j].index(".") != len(item[j]) - 1:
                flag.append(gotoFucntion(item[j]))

print("---------------------------------------------------------------")
print("Total States: ", len(flag))
for i in range(len(flag)):
    print(i, ":", flag[i])
print("---------------------------------------------------------------")


#Implementing DFA for LR0 Parsing

dfa = {}
for i in range(len(flag)):
    if i in dfa:
        pass
    else:
        lst = getList(dfaRules, i)
        samp = {}
        for j in lst:
            s = j.split()[1].split('->')[1]
            search = s[s.index('.') + 1]
            samp[search] = stateNumbers[str(dfaRules[j])]

        if samp != {}:
            dfa[i] = samp

print(dfa)

#DFA Implemented

#Implement Parsing Table

#-------------------- Constructing Basic Table -------------------
parsingTable = []
term = sorted(list(Terminals(productionRules)))
header = [''] * (len(term) + 1)
header[(len(term) + 1) // 2] = 'Action'

non_term = sorted(list(nonTerminals(productionRules)))
header2 = [''] * len(non_term)
header2[(len(non_term)) // 2] = 'Goto'

parsingTable.append([''] + term + non_term)

parsingTableDict = {}
#-------------------- Basic Construction Done -------------------

#String Parsing
for i in range(len(list)):
    data = [''] * (len(term) + len(non_term))
    samp = {}

    #Action
    try:
        for j in dfa[i]:
            if not j.isupper() and j != '' and j != '.':
                ind = term.index(j)
                data[ind] = 'S' + str(dfa[i][j])
                samp[term[ind]] = 'S' + str(dfa[i][j])

    except Exception:
        if i != 1:
            s = list(list[i][0])
            s.remove('.')
            s = "".join(s)
            lst = [i] + ['r' + str(productionNum[s])] * len(term)
            lst += [''] * len(non_term)
            parsingTable.append(lst)
            for j in term:
                samp[j] = 'r' + str(productionNum[s])
        else:
            lst = [i] + [''] * (len(term) + len(non_term))
            lst[-1] = 'Accept'
            parsingTable.append(lst)
    #goto
    try:
        for j in dfa[i]:
            if j.isupper():
                ind = non_term.index(j)
                data[len(term) + ind] = dfa[i][j]

                samp[j] = str(dfa[i][j])

        parsingTable.append([i] + data)
    except Exception:
        pass

    if samp == {}:
        parsingTableDict[i] = {'$': 'Accept'}
    else:
        parsingTableDict[i] = samp

#printing final table
final_table = tt.to_string(data=parsingTable, header=header + header2, style=tt.styles.ascii_thin_double, padding=(0, 1))

print("\n")
print(final_table)
print("\n")









#Program end