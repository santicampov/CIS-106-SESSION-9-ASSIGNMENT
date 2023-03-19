def compbavg(bat, nhit):
    batavg = bat / nhit
    
    return batavg

# Main
print("Enter player's last name.")
name = input()
print("Please enter the number of hits.")
nhit = float(input())
print("Please enter the at bats.")
bat = float(input())
compbavg(nhit, bat)
batavg = compbavg(nhit, bat)
print("For the player: " + name + ", the bat average is: " + str(batavg))