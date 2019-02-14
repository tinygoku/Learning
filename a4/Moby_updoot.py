def moby_discount( x ):
    regular = (x * 1.05)
    membership = (x * 0.735)
    print("Your total is: ${:.2f}".format(regular))
    print"Your total with a membership is: ${:.2f}".format(membership))
    print("You saved: ${:.2f}".format(regular - membership))

moby_discount(int(input("Total price of items: ")))
