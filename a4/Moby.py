def normal(price):
    return 1.05 * price
#function figures out price + tax
def discount(price):
    return (price * .85) * 1.05
#function for price with discount
price = float(input("Enter the value of your items: "))
normal_price = normal(price)
discount_price = discount(price)

print("Your total is:${0:.2f}".format(normal_price))
print("Total with Membership:${0:.2f}".format(discount_price))
print("You saved:${0:.2f}".format(normal_price - discount_price))

