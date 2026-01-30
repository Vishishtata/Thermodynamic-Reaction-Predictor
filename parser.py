# Feature 1 -  Feature 1: Reaction Input & Parsing
import re

reaction = input("Reaction(eg - 2H2 + O2 -> 2H2O) : ")
reaction = reaction.replace("→", "->")

pattern = r"->"
matches = re.finditer(pattern, reaction)

# splitting reactants and products
reactants = None
products = None

for match in matches :
   reactants = reaction[0:match.span()[0]]
   products = reaction[match.span()[1]: ]

reactants = reactants.split(r"+") #splitting reactants
products = products.split(r"+") # splitting products

reactants_dictionary = {}
products_dictionary = {}

# reactant dictionary
for item in reactants :
    item = item.strip()
    if item[0].isdigit :
        coeff = item[0]
        compound = item[1: ]
    else :
        coeff = 1
        compound = item[0: ]
    
    reactants_dictionary[compound] = coeff

# products dictionary
for item in products :
    item = item.strip()
    if item[0].isdigit :
        coeff = item[0]
        compound = item[1: ]
    else :
        coeff = 1
        compound = item[0: ]
    
    products_dictionary[compound] = coeff

print(reactants_dictionary.items())
print(products_dictionary.items())






