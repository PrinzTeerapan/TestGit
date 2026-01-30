Username = str(input("Enter your username: "))
Password = str(input("Enter your password: "))
if Username == "admin" and Password == "1234":
    print("-------COCOFRESH SHOP---------")
    print("1. Calculate VAT")
    print("2. price calculation")
    UserSelected = int(input("Select menu 1 or 2: "))
    if UserSelected == 1:
        price = float(input("Enter the price: "))
        vat = 7
        result = price + (price*vat/100)
        print(result)
    elif UserSelected == 2:
        Price1 = float(input("Enter price of item 1: "))
        Price2 = float(input("Enter price of item 2: "))
        total = Price1 + Price2
        print("Total price is:", total)
else:
    print("Invalid username or password.")