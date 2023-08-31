import stockread

def stockprint():
    """A function to print the inventory details in terminal in well formatted manner"""
    laptops = stockread.stockread()
    print("\nThe items in your stock are: \n\n")
    detailtopic = f'''
    {"S.No":>0}{"name":>18}{"brand":>19}{"Selling Price ($)":>28}{"Available qty":>20}{"Processor":>21}{"Graphics":>20}
    '''
    print(detailtopic)
    print("_"*140)
    for i in range (len(laptops)):
        if i+1 < 10:
            print(" ",i+1,end=" "*10)
        else:
            print(" ",i+1,end=" "*9)
        for j in range (len(laptops[i])):
            a =laptops[i][j]
            print("{:<21}".format("|    "+a),end="")
        print("\n")
    print("\n"+'"'*140)