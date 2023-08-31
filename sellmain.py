import os
import allBillprint
import stockread
laptops = stockread.stockread()
def sell_again_and_again(billdetails,CustomerName,billdatetime):
        """A function to to make the sell again and again"""
        

        again = input("Do you want to sell again? Type (yes) or (no): ").lower()
        if again == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            sellnum,quantity = laptopdetail()
            sellmenu(sellnum,quantity)
            billdetails.append([laptops[sellnum-1][0],laptops[sellnum-1][1],laptops[sellnum-1][2],quantity,int(laptops[sellnum-1][2])*(quantity)])
            sell_again_and_again(CustomerName,billdatetime,billdatetime)


        elif again == "no":
            allBillprint.sell_item_print(billdetails,CustomerName,billdatetime)    
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t\t\t\tThank You For Your Sell\n")
            print("\t\t\t\t\t Your customer bill is: ")
            allBillprint.sellbillshow(CustomerName,billdatetime)
            

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            allBillprint.sell_item_print(billdetails,CustomerName,billdatetime)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t\t\t\tThank You For Your Sell")
            print("\t\tYour further more sell is terminated Due to wrong key press ! ! !\n")
            allBillprint.sellbillshow(CustomerName,billdatetime)
        



def sellmenu(sellnum,quantity):
    """A function for all operations of purchase of laptops from manufacturers"""
    import stockread  
    laptops = stockread.stockread()

    with open('inventory.txt', 'w') as file:
        for a in range (len(laptops)):
            for b in range (len(laptops[a])):
                if a == sellnum-1 and b == 3:
                    addedqty = int(laptops[a][b])-quantity
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
    sellnumboolean = True
    while sellnumboolean:
        sellnum = input("Please select the Laptop's S.No which you want to sell:  ")
        if sellnum.isdigit():
            if int(sellnum)<=int(len(laptops)) and int(sellnum) >=1:
                break
            else:
                print("Please enter laptops within stock range ! ! ! ")
        else:
            print("Please enter valid numeric value ! ! ! ")
    
    quantityboolean = True
    while quantityboolean:
        quantity = input("Enter the quantity of that laptop you want to sell:  ")
        if quantity.isdigit() and int(quantity)>=1:
            if int(quantity) <= int(laptops[int(sellnum)-1][3]):
                break
            else:
                print(f"The stock number of selected laptop is only: {laptops[int(sellnum)-1][3]} Please select within available stock. ")
        else:
            print("Please Enter valid numeric value ! ! !")
    return int(sellnum),int(quantity)
