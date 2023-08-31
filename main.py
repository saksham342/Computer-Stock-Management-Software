import firstinterface
import os
import buymain
import sellmain
import stockread
import allBillprint
laptops = stockread.stockread()

#Importing data and time
import datetime
present = datetime.datetime.now()
insidebilldatetime = present.strftime("%Y-%m-%d_%H:%M:%S") #converting date and time into string format
billdatetime = present.strftime("%Y-%m-%d_%H-%M-%S.txt")

firstinterface.maindisplay()

def maincondition():
    """A function for the selection of 4 main options, also have functions to sell and buy again and again """

    def buy_again_and_again():
        """A function to buy items again and again from manufacturer"""
        again = input("Do you want to buy again:? Type (yes) or (no): ").lower()
        if again == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            buynum,quantity = buymain.laptopdetail()
            buymain.buymenu(buynum,quantity)
            billdetails.append([laptops[buynum-1][0],laptops[buynum-1][1],str(int(laptops[buynum-1][2])*0.6),quantity,(int(laptops[buynum-1][2]))*0.6*(quantity)])
            buy_again_and_again()


        elif again == "no":
            allBillprint.buy_item_print(billdetails,DistributorName, billdatetime)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t\t\t\tThank You For Your Purchase\n")
            allBillprint.purchasebillshow(DistributorName,billdatetime)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            allBillprint.buy_item_print(billdetails,DistributorName, billdatetime)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t\t\t\tThank You For Your Purchase")
            print("\t\t\tYour further more purchase is terminated Due to wrong key press ! ! ! \n")
            allBillprint.purchasebillshow()

        firstinterface.maindisplay()
        maincondition()


    def sell_again_and_again():
        """A function to to make the sell again and again"""
        

        again = input("Do you want to sell again? Type (yes) or (no): ").lower()
        if again == "yes":
            os.system('cls' if os.name == 'nt' else 'clear')
            sellnum,quantity = sellmain.laptopdetail()
            sellmain.sellmenu(sellnum,quantity)
            billdetails.append([laptops[sellnum-1][0],laptops[sellnum-1][1],laptops[sellnum-1][2],quantity,int(laptops[sellnum-1][2])*(quantity)])
            sell_again_and_again()


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
        firstinterface.maindisplay()
        maincondition()
    

    #Getting selection number as input to redirect to respective functions.
     
    try: 
        mainselect= int(input("Please enter your selection: "))
    except ValueError:
        print("\nPlease enter a numeric value: ")
        firstinterface.maindisplay()
        maincondition()

    if mainselect == 1:
        DistributorName = input("Please enter the name of Distributor: ")
        if  (''.join(DistributorName.split())).isalpha():
            allBillprint.bill_buy_topic(DistributorName, billdatetime,insidebilldatetime )
            os.system('cls' if os.name == 'nt' else 'clear')
            buynum,quantity = buymain.laptopdetail()
            buymain.buymenu(buynum,quantity)
            billdetails = []
            billdetails.append([laptops[buynum-1][0],laptops[buynum-1][1],(int(laptops[buynum-1][2])*0.6),quantity,int(laptops[buynum-1][2])*0.6*(quantity)])
            buy_again_and_again()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("       Purchase is terminated due to invalid Distributer name.")
            print("\n")
            print("Select sell option again and provide the valid Distributor name ! ! !")
            print("\n")
        firstinterface.maindisplay()
        maincondition()


    elif mainselect == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        import stockshow
        stockshow.stockprint()
        key = input("Press Enter key to go main display: ")
        if (key == "                       "):
            pass
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            firstinterface.maindisplay()
            maincondition()


    elif mainselect == 3:
        CustomerName = input("Please enter the name of customer: ")
        if  (''.join(CustomerName.split())).isalpha():
            allBillprint.bill_sell_topic(CustomerName,billdatetime,insidebilldatetime)
            os.system('cls' if os.name == 'nt' else 'clear')
            sellnum,quantity = sellmain.laptopdetail()
            sellmain.sellmenu(sellnum,quantity)
            billdetails = []
            billdetails.append([laptops[sellnum-1][0],laptops[sellnum-1][1],laptops[sellnum-1][2],quantity,int(laptops[sellnum-1][2])*(quantity)])
            sell_again_and_again()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("        Sell is terminated due to Invalid customer name.")
            print("\n")
            print("Select sell option again and provide the valid customer name ! ! !")
            print("\n")
        firstinterface.maindisplay()
        maincondition()   


    elif mainselect == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your software is exited.\nThank you for using it.  ")
    
        exit()


    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n! ! ! Please Enter a valid Selection from 1 to 4 only! ! !")
        firstinterface.maindisplay()
        maincondition()
maincondition()
