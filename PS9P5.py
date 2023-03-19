def comptuition(credits, code):
    if code == "I":
        tuition = credits * 250
    else:
        tuition = credits * 550
    
    return tuition

# Main
print("Please enter the student's last name.")
name = input()
print("Please enter the amount of credit hours the student is taking.")
credits = float(input())
print("Is the student In District or Out of district?(please enter I or O)")
code = input()
comptuition(credits, code)
tuition = comptuition(credits, code)
print("For the student " + name + ", the tuition owed is: $" + str(tuition))