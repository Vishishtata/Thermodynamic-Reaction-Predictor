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

reactants = reactants.strip()
products = products.strip()

pattern2 = r"\+"

# Separating reactants
matches_reactants = re.finditer(pattern2, reactants)

for match in matches_reactants :
    reactants_left = reactants[0:match.span()[0]]
    reactants_right = reactants[match.span()[1]: ]
    reactants = reactants_left + reactants_right 
# Separate products
matches_products = re.finditer(pattern2, products)

for match in matches_products :
   products_left = products[0:match.span()[0]]
   products_right = products[match.span()[1]: ]
   products = products_left + products_right 





print(f"Reactants : {reactants}")
print(f"Products : {products}")

