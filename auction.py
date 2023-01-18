import os
print()
print("▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇")
print("▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇")
print("▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇")
print("▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇")
print("▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇")
print("▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇")
print("▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇")
print("▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇")
print()
print("This is an auction!")

bids = {}
choice = input("Would you like to add a bid?(YES/NO): ")
if choice.upper() == "NO":
    running = False
else:
    running = True
while running:
    name = input("Insert the name: ")
    bid = input("Insert the bid: $")
    bids[name]=bid
    choice = input("Would you like to add a bid?(YES/NO): ")
    os.system('clear')
    if  choice.upper() == "NO":
        running = False

maximum = 0
for key in bids:
    if int(bids[key])>maximum:
        maximum = int(bids[key])
        maxname = key
        
print(f"{maxname} won the bidding, with a bid of {maximum}")