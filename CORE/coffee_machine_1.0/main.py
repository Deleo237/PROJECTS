#COFFEE MACHINE
#ALT + SHIFT
from artword import MENU,resources

def mon():
    a=int(input("How many quarters?: "))
    b=int(input("How many dimes?: "))
    c=int(input("How many nickles?: "))
    d=int(input("How many pennies?: "))
    e=(a*0.25)+(b*0.1)+(c*0.05)+(d*0.01)
    f=round(e,2)
    return f

def check(type):
    """Selects the type of coffee and check if available"""
    i=MENU[type]
    ing=i["ingredients"]
    if ing["water"]>resources["water"]:
        return "Sorry there is not enough water"
    elif ing["milk"]>resources["milk"]:
        return "Sorry there is not enough milk"
    elif ing["coffee"]>resources["coffee"]:
        return "Sorry there is not enough coffee"
    else:
        print("Please insert coins.")
        m=mon()
        if m<i["cost"]:
            return "Sorry that's not enough money. Money Refunded"
        else:
            resources["water"]-=ing["water"]
            resources["milk"]-=ing["milk"]
            resources["coffee"]-=ing["coffee"]
            resources["cost"]+=i["cost"]
            print(f'Here is your balance of ${m-i["cost"]}')
            return f"Here is your {type} ☕️ Enjoy!" 
        
def report(res):
    """Display the report"""
    print(f'Water: {res["water"]}ml')
    print(f'Milk: {res["milk"]}ml')
    print(f'Coffe: {res["coffee"]}g')
    print(f'Money: ${res["cost"]}')
    
    
    
q=1     
while q==1:
    print("WELCOME TO MY GITHUB 'coffee machine 1.0' PROJECT.")
    ans=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if ans=="espresso":
        print(check(ans))
    elif ans=="latte":
        print(check(ans))
    elif ans=="cappuccino":
        print(check(ans))
    elif ans=="report":
        report(resources)
    elif ans=="off":
        q=0
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!MACHINE SHUTING DOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("<<<<<<<<<<<<<<<< WRONG INPUT >>>>>>>>>>>>>>")