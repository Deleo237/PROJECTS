#Bill splitting
print("WELCOME TO MY GITHUB 'calculator 1.0' PROJECT.")
b=float(input("Welcome to the tip calculator.\nWhat was the total bill? $"))
t=float(input("What percentage tip would you like to give? 10, 12, or 15? "))
a=b+(b*t/100)
p=float(input("How many people to slit the bill? "))
print(f"Each person should pay: ${round(a/p,2)}")