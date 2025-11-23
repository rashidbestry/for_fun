import time

resources = {"Water":[300,"ml"],"Milk":[200,"ml"],"Coffee":[100,"gr"],"Money":[2.5,"$"]}
prices = {"espresso":1.50,"latte":2.50,"cappuccino":3.00}
coins = {"penny":0.01,"Nickel":0.05,"Dime":0.1,"Quarter":0.25}
coffees = ("espresso","latte","cappuccino")

def get_order(coffees):
        while True:
            print()
            order = input(f"What would you like? {coffees} ☕: ")
            if order not in ("espresso","latte","cappuccino","off","report"):
                print("\nI did not understand, please try again!\n")
                continue
            if order=="report":
                for i in resources.items():
                    print(f"{i[0]} : {i[1][0]} {i[1][1]}")
            else:
                break

        return order

def check_order(order):
    print("Thank you for your order! Let me check!")
    for i in range(5):
        print(">", end=">")
        time.sleep(0.5)
    have_resources = check_resources(order)
    if have_resources==True:
        return order
    else:
        can_offer = []
        print(f"\nSorry I don't have enough {have_resources.split("&")[1::]} to make a {order} ☕!")
        print("\nPlease wait! I’m seeing what can i do for you!\n")
        for i in range(5):
            print(">>>>>", end=">>>>>")
            time.sleep(0.5)

        for cof in ["espresso","latte","cappuccino"]:
            if cof == order: continue
            if check_resources(cof)==True:
                can_offer.append(cof)
        if len(can_offer) != 0:
            print("\n\nI have enough resources to make these coffees: \n")
            return get_order((can_offer[::]))
        if len(can_offer) == 0:
            print("\nSorry sir currently we out of resources, come back later!\n")
            return False

def check_resources(order):
    have_resources = True
    absent_resources = ""
    if order == "espresso":
        if resources["Water"][0] - 50 < 0:
            absent_resources += "&Water,"
        if resources["Coffee"][0] - 18 < 0:
            absent_resources += "&Coffee,"
    if order == "latte":
        if resources["Water"][0] - 200 < 0:
            absent_resources += "&Water,"
        if resources["Milk"][0] - 150 < 0:
            absent_resources += "&Milk"
        if resources["Coffee"][0] - 24 < 0:
            absent_resources += "&Coffee"
    if order == "cappuccino":
        if resources["Water"][0] - 250 < 0:
            absent_resources += "&Water"
        if resources["Milk"][0] - 100 < 0:
            absent_resources += "&Milk"
        if resources["Coffee"][0] - 24 < 0:
            absent_resources += "&Coffee"
    return absent_resources if len(absent_resources)>1 else have_resources

def taking_cash(ordered):
    print("\nPlease insert coins!")
    while True:
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            print("\nWait a minute!")
            for i in range(5):
                print(">>>>>", end=">>>>>")
                time.sleep(0.5)
        except:
            print("Please insert only coins!")
        finally:
            sum = round(quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01,2)
            if sum > prices[ordered]:
                print(f"\nHere is {sum-prices[ordered]} in change")
                resources["Money"][0] += prices[ordered]
                print(f"\nHere is your {ordered} ☕ Enjoy!\n")
                break

            else:
                print("Sorry that's not enough money. Money refunded! ")
                launcher()
    return True

def take_resources(order):
    if order == "espresso":
        resources["Water"][0] -= 50
        resources["Coffee"][0] -= 18
    if order == "latte":
        resources["Water"][0] -= 200
        resources["Milk"][0] -= 150
        resources["Coffee"][0] -= 24
    if order == "cappuccino":
        resources["Water"][0] -= 250
        resources["Milk"][0] -= 100
        resources["Coffee"][0] -= 24

def launcher():
    order = get_order(coffees)
    if order == "off":
        print("The machine is turning off ", end="")
        for i in range(5):
            print("!",end="")
            time.sleep(0.5)
        return
    ordered = check_order(order)
    cash_taken=False
    if ordered:
       cash_taken = taking_cash(ordered)
    if cash_taken:
        take_resources(ordered)
    launcher()

if __name__=="__main__":
    launcher()