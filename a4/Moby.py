def moby_discount( x ):
    regular = (x * 1.05)
    membership = (x * 0.735)
    print("Your total is %.2f", regular)
    print("Your total with a membership $", membership)
    print("you saved $ ", regular - membership)


moby_discount(int(input("Total price of items ")))