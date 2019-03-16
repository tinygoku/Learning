def normal(price):
    return 1.05 * price

def discount(price):
    return (price * .85) * 1.05

price = float(input("Enter the value of your items: "))
normal_price = normal(price)
discount_price = discount(price)

print("Your total is:$ ", normal_price)
print("Total with Membership:$ ", discount_price)
print("You saved:$", normal_price - discount_price)

# decimals, only on print line.
