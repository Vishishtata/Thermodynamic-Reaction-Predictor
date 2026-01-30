# Feature 1 -  Feature 1: Reaction Input & Parsing
import re
import time

while True :
    reaction = input("Reaction(eg - 2H2 + O2 -> 2H2O) : ")
    reaction = reaction.replace("→", "->")
    arrow_count = reaction.count("->")

    if arrow_count != 1 :
        print("Reaction must contain only one arrow!!")
        time.sleep(2)
        continue
    

    pattern = r"->"
    matches = re.finditer(pattern, reaction)

    # splitting reactants and products
    reactants = None
    products = None

    for match in matches :
        reactants = reaction[0:match.span()[0]]
        products = reaction[match.span()[1]: ]

    reactants = reactants.split("+") #splitting reactants
    products = products.split("+") # splitting products

    reactants_dictionary = {}
    products_dictionary = {}

    # reactant dictionary
    for item in reactants :
        item = item.strip()
        if not item :
            continue

        if item[0].isdigit():
            coeff = int(item[0])
            compound = item[1: ]
        else :
            coeff = 1
            compound = item[0: ]

        if not compound :
            print("Invalid reaction Format!")
            time.sleep(2)
            continue
        

        reactants_dictionary[compound] = coeff

    # products dictionary
    for item in products :
        item = item.strip()
        if not item :
            continue

        if item[0].isdigit():
            coeff = int(item[0])
            compound = item[1: ]
        else :
            coeff = 1
            compound = item[0: ]

        if not compound :
            print("Invalid reaction Format!")
            time.sleep(2)
            continue
        
    
        products_dictionary[compound] = coeff
    break






