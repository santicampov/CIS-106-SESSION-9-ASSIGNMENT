def cmptotal(price, qty):
    total = qty * price
    if total > 10000:
        total = total * 0.9
    
    return total

# Main
print("Please enter the quantity.")
qty = float(input())
print("Please enter the price of the item.")
price = float(input())
cmptotal(qty, price)
total = cmptotal(qty, price)
print("For the purchase, the number of items ordered is: " + str(qty) + ", and a price per unit of: $" + str(price) + "; The total is:  $" + str(total))