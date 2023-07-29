from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
C=CoffeeMaker()
M=Menu()
#MI=MenuItem()
MM=MoneyMachine()
def allall(tea):
    r=M.find_drink(tea)
    if C.is_resource_sufficient(r) is True:
        if MM.make_payment(r.cost) is True:
            C.make_coffee(r)
q=1
while q==1:
    i=M.get_items()
    print("WELCOME TO MY GITHUB 'coffee machine 1.1' PROJECT.")
    ans=input(f"What would you like? ({i}): ").lower()
    if ans=="espresso":
        allall(ans)
    elif ans=="latte":
        allall(ans)
    elif ans=="cappuccino":
        allall(ans)
    elif ans=="report":
        C.report()
        MM.report()
    elif ans=="search":
        t=input(f"What tea do you want do search about?: ").lower()
        r=M.find_drink(t)
        if r!=None:
            print(f"Yes {t} tea is available")
    elif ans=="off":
        q=0
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!MACHINE SHUTING DOWN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("<<<<<<<<<<<<<<<< WRONG INPUT >>>>>>>>>>>>>>")