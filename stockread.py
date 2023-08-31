def stockread():
    """A function to read the inventory details and store in variable 'alllaptops'"""
    alllaptops = []
    with open('inventory.txt','r') as stock:
        for line in stock:
            lines = ((line.strip()).split(","))
            alllaptops.append(lines)
    return alllaptops
