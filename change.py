# change.py
# a program to calculate the value of some chage in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")
    quarters = int(input("Quarters:"))
    dimes = int(input("Dimes:"))
    nickles = int(input("Nickels:"))
    pennies = int(input("Pennies:"))
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    print()
    print("the total value of your change is", total)

main()

