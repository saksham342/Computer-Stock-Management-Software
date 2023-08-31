def buymenu(buynum,quantity):
    """A function for all operations of purchase of laptops from manufacturers"""
    import stockread  
    laptops = stockread.stockread()

    with open('inventory.txt', 'w') as file:
        for a in range (len(laptops)):
            for b in range (len(laptops[a])):
                if a == buynum-1 and b == 3:
                    addedqty = int(laptops[a][b])+quantity
                    file.write(str(addedqty) +",")
                elif b == 5:
                    file.write(str(laptops[a][5]))
                else:
                    file.write(str(laptops[a][b]) +",")
            file.write("\n")


def laptopdetail():
    import stockshow, stockread
    laptops = stockread.stockread()
    stockshow.stockprint() 
    buynumboolean = True
    while buynumboolean:
        buynum = input("Please select the Laptop's S.No which you want to buy:  ")
        if buynum.isdigit():
            if int(buynum)<=int(len(laptops)) and int(buynum) >=1:
                break
            else:
                print("Please enter laptops within stock range ! ! ! ")
        else:
            print("Please enter valid numeric value ! ! ! ")
    
    quantityboolean = True
    while quantityboolean:
        quantity = input("Enter the quantity of that laptop you want to buy:  ")
        if quantity.isdigit() and int(quantity)>=1:
            break
        else:
            print("Please Enter valid numeric value ! ! !")
    return int(buynum),int(quantity)
