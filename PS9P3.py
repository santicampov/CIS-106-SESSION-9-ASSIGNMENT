def compcost(gallons):
    cost = gallons * 2.5
    
    return cost

def compmpg(miles, gallons):
    mpg = miles / gallons
    
    return mpg

# Main
print("Please enter the destination city.")
city = input()
print("Please enter the number of miles traveled.")
miles = float(input())
print("How many gallons of gas did you use for this trip.")
gallons = float(input())
compmpg(miles, gallons)
mpg = compmpg(miles, gallons)
compcost(gallons)
cost = compcost(gallons)
print("For the destination : " + city + ", with the distance of: " + str(miles) + " miles. The miles per gallon is: " + str(mpg) + " mpg. With the total cost of: $" + str(cost))