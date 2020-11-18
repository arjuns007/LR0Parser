#Importing Necessary Libraries

import os
from collections import Counter
import pyfiglet
import termtables as tt



if __name__ == '__main__':
    prod = []
    set_of_items = []
    c = []


    result = pyfiglet.figlet_format("LR (0) Parsing", font="epic")
    print(result)

    num = int(input("Enter grammar number: "))
    print("\n")

    with open("grammar/" + str(num) + ".txt", 'r') as fp:
        for i in fp.readlines():
            prod.append(i.strip())
    prod.insert(0, "X->.S")
    print("---------------------------------------------------------------")
    print("Augmented Grammar")
    print(prod)

    prod_num = {}
    for i in range(1, len(prod)):
        prod_num[str(prod[i])] = i

    j = closure("X->.S")
    set_of_items.append(j)

    state_numbers = {}
    dfa_prod = {}
    items = 0