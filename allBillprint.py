def bill_buy_topic(DistributorName, billdatetime,insidebilldatetime ):
      with open(f"{DistributorName}{billdatetime}", "w") as billfile:
                billtitle = f"""
            {"*" * 82}
            |{"TechChip Computers".center(80)}{"|":>0}
            {"-" * 82}
            |{"Distributor's Invoice".center(80)}{"|":>0}
            {"*" * 82}
            Distributor's name: {DistributorName}
            Date_Time: {insidebilldatetime}

            {"{:<19}{:<19}{:<19}{:<19}{:<19}".format("Name", "Brand", "Rate($)", "Quantity", "Total($)")}

            """
                billfile.write(billtitle)


def buy_item_print(billdetails,DistributorName, billdatetime):
                """A function to print the text bill"""
                uptosum = 0
                for i in range(len(billdetails)):
                    uptosum += int(billdetails[i-1][4])
                with open(f"{DistributorName}{billdatetime}", "a") as billprint:
                    for eachline in billdetails:
                        for eachword in eachline:
                            billprint.write("{:<19}".format(str(eachword)))
                        billprint.write("\n"+(" "*12))
                    last_sum = f"""
                                                                                        {("______")}
                                                                                    = $ {(uptosum)}
                                                                    VAT amount (13%): $ {0.13*uptosum}
                                                                        total cost  : $ {uptosum+0.13*uptosum}
            {"_"*81}  
            |{"The following items purchased successfully ! ! !".center(80)}{"|":>0}                                                             
            {"*"*81}
                    """
                    billprint.write(last_sum)


def bill_sell_topic(CustomerName,billdatetime,insidebilldatetime):
       with open(f"{CustomerName}{billdatetime}", "w") as billfile:
                billtitle = f"""
            {"*" * 82}
            |{"TechChip Computers".center(80)}{"|":>0}
            {"-" * 82}
            |{"Customer Invoice".center(80)}{"|":>0}
            {"*" * 82}
            Customer's name: {CustomerName}
            Date_Time: {insidebilldatetime}

            {"{:<19}{:<19}{:<19}{:<19}{:<19}".format("Name", "Brand", "Rate($)", "Quantity", "Total($)")}

            """
                billfile.write(billtitle)


def sell_item_print(billdetails,CustomerName,billdatetime):
                """A function to print the text bill"""
                uptosum = 0
                for i in range(len(billdetails)):
                    uptosum += int(billdetails[i-1][4])
                with open(f"{CustomerName}{billdatetime}", "a") as billprint:
                    for eachline in billdetails:
                        for eachword in eachline:
                            billprint.write("{:<19}".format(str(eachword)))
                        billprint.write("\n"+(" "*12))
                    last_sum = f"""
                                                                                        {("______")}
                                                                                    =  $ {(uptosum)}
                                                                        shipping cost: $ 7
                                                                           total cost: $ {uptosum+7}
            {"_"*81}  
            |{"Thank you for purchase. Visit us again ! ! !".center(80)}{"|":>0}                                                             
            {"*"*81}
                    """ 
                    billprint.write(last_sum)


def purchasebillshow(DistributorName,billdatetime):
    """A function to show printed bill in shell/terminal"""
    with open(f"{DistributorName}{billdatetime}", "r") as purchasebillshow:
        for line in purchasebillshow:
            print(line)

def sellbillshow(CustomerName,billdatetime):
    with open(f"{CustomerName}{billdatetime}", "r") as sellbillshow:
        for line in sellbillshow:
            print(line)