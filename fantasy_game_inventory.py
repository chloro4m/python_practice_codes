#given ANY dictionary, e.g.:
#{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#print like this:
##Inventory:
##12 arrow
##42 gold coin
##1 rope
##6 torch
##1 dagger
##Total number of items: 62


###supressing codes (see ##) below to use this program as imported module
##stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, \
##         'dagger': 1, 'arrow': 12}

def displayInv(inv):
    print('Inventory:')
    total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total number of items: ' + str(total))
    

#main program
##displayInv(stuff)
