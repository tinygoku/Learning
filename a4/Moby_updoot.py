"""def moby_discount( x ):
    regular = (x * 1.05)
    membership = (x * 0.735)
    print("Your total is: ${:.2f}".format(regular))
    print"Your total with a membership is: ${:.2f}".format(membership))
    print("You saved: ${:.2f}".format(regular - membership))

moby_discount(int(input("Total price of items: ")))"""

# String theory 101

string_1 = "Julian"
string_2 = "Moke"
string_3 = "Wow {} is really cool!"
string_4 = "{} != {}"

print(string_1)
print(string_2 + string_1)
print(string_3.format(string_1))
print(string_4.format(3, 4))
print(string_4.format(string_1, string_2))

print(string_4.format(string_3.format(string_2), string_2))
