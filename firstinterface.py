def maindisplay():
    """A function to display the 4 options in well format"""
    main = f"""
                   "Welcome to TechChip Computers"
    {"*" * 60}
    |{"TechChip Computers".center(58)}{"|":>0}
    {"*" * 60}
    |{"|":>59}
    |{"|":>59}
    |{" ":>17}{"1. Buy From Manufacturer"}{"|":>18}
    |{"|":>59}
    |{" ":>17}{"2. View Stock"}{"|":>29}
    |{"|":>59}
    |{" ":>17}{"3. Sell to Customers"}{"|":>22}
    |{"|":>59}
    |{" ":>17}{"4. Exit"}{"|":>35}
    |{"|":>59}
    {'"'*60}
    """
    print(main)
    
