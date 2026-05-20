# Feature 1 -  Feature 1: Reaction Input & Parsing
import re
import time


print("Thermodynamic Reaction Predictor...")
time.sleep(2)
print('''1. Provide Reaction
2. Provide Reactants ''')
choice = int(input("Choose.."))

while True :
    if choice == 1:
        reaction = input("Reaction(eg - 2H2 + O2 -> 2H2O) : ")
        reaction = reaction.replace("→", "->")
        arrow_count = reaction.count("->")

        if arrow_count != 1 :
            print("Reaction must contain only one arrow!!")
            time.sleep(4)
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

        reactants_dictionary = {} # coiff is value and reactant is the key
        products_dictionary = {}

        # reactant dictionary
        for item in reactants :
            item = item.strip()
            if not item :
                continue

            n = 0
            for i in range(len(item)) :
                if item[i].isdigit() :
                    n = n + 1
                else :
                    break
            if n > 0:
                coeff = int(item[0:n])
                compound = item[n: ]
            else :
                coeff = 1
                compound = item[0: ]

            if not compound :
                print("Invalid reaction Format!")
                time.sleep(3)
                continue
            

            reactants_dictionary[compound] = coeff

        # products dictionary
        for item in products :
            item = item.strip()
            if not item :
                continue

            n = 0
            for i in range(len(item)) :
                if item[i].isdigit() :
                    n = n + 1
                else :
                    break
            if n > 0:
                coeff = int(item[0:n])
                compound = item[n: ]
            else :
                coeff = 1
                compound = item[0: ]

            if not compound :
                print("Invalid reaction Format!")
                time.sleep(3)
                continue
            
        
            products_dictionary[compound] = coeff
        break

    elif choice == 2:
        reactants = input("Enter all the reactants(separate by a comma) : ").split(",")
        products = input("Enter all the products(separate by a comma) : ").split(",")

        reactants_dictionary = {} # coiff is value and reactant is the key
        products_dictionary = {}

        for item in reactants :
            item = item.strip()
            if not item :
                continue

            n = 0
            for i in range(len(item)) :
                if item[i].isdigit() :
                    n = n + 1
                else :
                    break
            if n > 0:
                coeff = int(item[0:n])
                compound = item[n: ]
            else :
                coeff = 1
                compound = item[0: ]

            if not compound :
                print("Invalid reaction Format!")
                time.sleep(3)
                continue
            reactants_dictionary[compound] = coeff


        for item in products :
            item = item.strip()
            if not item :
                continue

            n = 0
            for i in range(len(item)) :
                if item[i].isdigit() :
                    n = n + 1
                else :
                    break
            if n > 0:
                coeff = int(item[0:n])
                compound = item[n: ]
            else :
                coeff = 1
                compound = item[0: ]

            if not compound :
                print("Invalid reaction Format!")
                time.sleep(3)
                continue
            
        
            products_dictionary[compound] = coeff
        break
        
        

print(reactants_dictionary)
print(products_dictionary)




