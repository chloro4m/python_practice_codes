import fantasy_game_inventory #i wrote this code alrdy

def addToInv(inventory, loot): #returns updated inv. dict.
    #code
    for i in range(0, len(loot)):
        if (loot[i] in inventory):
            inventory[loot[i]] += 1 #scrutinize?
        else:
            inventory[loot[i]] = 1
    return inventory
            

#main program
inv = {'gold coin': 42, 'rope': 1}
print('This is what you have so far in your inventory: ')
fantasy_game_inventory.displayInv(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', \
              'gold coin', 'ruby']

print('This is the loot dropped by the dragon: ')
for i in range(0, len(dragonLoot)):
    print(dragonLoot[i])
    
print('Here is your updated inventory: ')
newInv = addToInv(inv, dragonLoot)
fantasy_game_inventory.displayInv(newInv)
