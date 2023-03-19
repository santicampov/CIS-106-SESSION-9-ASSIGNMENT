def compgross(hours, rate):
    if hours > 40:
        overtime = hours - 40
        gpay = (hours - overtime) * rate + overtime * (rate * 1.5)
    else:
        gpay = hours * rate
    
    return gpay

def comprate(code):
    if code == "L":
        rate = 25
    else:
        if code == "A":
            rate = 30
        else:
            if code == "J":
                rate = 50
            else:
                print("Incorrect Job code, please restart the program.")
    
    return rate

# Main
print("Please enter your last name.")
name = input()
print("Please select one of the following job codes:( L - A - J )")
code = input()
print("Please enter the amount of hours worked.")
hours = float(input())
comprate(code)
rate = comprate(code)
compgross(hours, rate)
gpay = compgross(hours, rate)
print("For " + name + ", the gross pay is: $" + str(gpay))