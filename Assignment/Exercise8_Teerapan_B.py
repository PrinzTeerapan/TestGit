Username = str(input("Enter your username: "))
Password = str(input("Enter your password: "))
if Username == "customer" and Password == "1111":
    print("-------------COCOFRESH SHOP--------------")
    print("MENU")
    print("1.Smoothies Coconut              : 40 THB")
    print("2.Strawberry Smoothies Coconut   : 45 THB")
    print("3.Logan Smoothies Coconut        : 45 THB")
    print("4.Freshed Coconut                : 25 THB")
    print("5.CocaCola Coconut               : 45 THB")
    print("6.CocaCola                       : 20 THB")
    print("7.Water                          : 10 THB")
    print("8.Mineral Water                  : 15 THB")
    print("-----------------------------------------")   
    print("Select menu 1-8")
    UserSelected = int(input("Menu : "))
    if UserSelected == 1:
        Qty1 = int(input("How many do you want? : "))
        total1 = Qty1 * 40
        print("Total price is:", total1, "THB")
    elif UserSelected == 2:
        Qty2 = int(input("How many do you want? : "))
        total2 = Qty2 * 45
        print("Total price is:", total2, "THB")
    elif UserSelected == 3:
        Qty3 = int(input("How many do you want? : "))
        total3 = Qty3 * 45
        print("Total price is:", total3, "THB")
    elif UserSelected == 4:
        Qty4 = int(input("How many do you want? : "))
        total4 = Qty4 * 25
        print("Total price is:", total4, "THB")
    elif UserSelected == 5:
        Qty5 = int(input("How many do you want? : "))
        total5 = Qty5 * 45
        print("Total price is:", total5, "THB")
    elif UserSelected == 6:
        Qty6 = int(input("How many do you want? : "))
        total6 = Qty6 * 20
        print("Total price is:", total6, "THB")
    elif UserSelected == 7:
        Qty7 = int(input("How many do you want? : "))
        total7 = Qty7 * 10
        print("Total price is:", total7, "THB")
    elif UserSelected == 8:
        Qty8 = int(input("How many do you want? : "))
        total8 = Qty8 * 15
        print("Total price is:", total8, "THB")
else:
    print("Invalid username or password.")