from prettytable import PrettyTable
from time import sleep

class Coffee:
    def __init__(self,name):
        self.name = name

class Coin:
    def __init__(self,name,value):
        self.name = name
        self.value = value

class CoffeeMachine:

    def __init__(self):
        self.resources = {"Water": 300, "Milk": 200, "Coffee": 100, "Money": 2.5}
        self.resources_consume = {"espresso": {"Water": 50,"Milk":0 ,"Coffee":18}, "latte": {"Water": 200,"Milk": 150,"Coffee":24}, "cappuccino": {"Water":250,"Milk":100,"Coffee":24}}
        self.coins = {"penny": 0.01, "Nickel": 0.05, "Dime": 0.1, "Quarter": 0.25}
        self.prices = {"espresso":1.50, "latte":2.50, "cappuccino":3.00}
        self.available_coffees = ["espresso","latte","cappuccino"]

    def get_order(self):
        while True:
            table_0 = PrettyTable()
            table_0.add_column("Coffees",self.available_coffees)
            table_0.add_column("Prices",[self.prices[coffee] for coffee in self.available_coffees])
            order = input(f"{table_0}\n What would you like?  ☕: ")
            if order not in ("espresso", "latte", "cappuccino", "off", "report"):
                print("I did not understand, please try again!")
                continue
            elif order == "report":
                table = PrettyTable()
                table.add_column("Resources",["Water", "Milk", "Coffee", "Money"])
                resource = self.resources
                table.add_column("Amount",[resource["Water"], resource["Milk"], resource["Coffee"], resource["Money"]])
                table.add_column("Unit",["ml", "ml", "gr", "$"])
                print(table)
                input("***********************")
                continue
            elif order == "off":
                print("The Coffee Machine is turning off!!!")
                for i in range(10):print(">>",end=""),sleep(0.3)
                return "off"
            return order
    def check_resources(self,order):
        insufficient = set()
        if self.resources["Water"] - self.resources_consume[order]["Water"] < 0:
            insufficient.add("Water")
        elif self.resources["Milk"] - self.resources_consume[order]["Milk"] < 0:
            insufficient.add("Milk")
        elif self.resources["Coffee"] - self.resources_consume[order]["Coffee"] < 0:
            insufficient.add("Coffee")
        if len(insufficient)>0:
            print(f"\nSorry currently machine out of {insufficient}")
            return False
        return True
    def check_available_coffees(self):
        print("Let me check what i can do for you!")
        for i in range(10): print(">>", end=""), sleep(0.3)
        available_coffees = []
        for coffee in self.prices.keys():
            if not self.check_resources(coffee):
                continue
            else:
                available_coffees.append(coffee)
        if len(available_coffees)>0:
            print("I have enough resources to make these coffees:")
            self.available_coffees = available_coffees
            return True
        if len(available_coffees)==0:
            print("\nSorry sir currently we out of resources, come back later!")
            return False
    def take_cash(self,order):
        sum_coins = 0
        while True:
            coins = []
            try:
                for coin in range(int(input("\nHow many quarters?: "))):
                    quarter = Coin("Quarter",0.25)
                    coins.append(quarter)
                for coin in range(int(input("How many dimes?: "))):
                    dimes = Coin("Dimes",0.1)
                    coins.append(dimes)
                for coin in range(int(input("How many nickles?: "))):
                    nickles = Coin("Nickles",0.05)
                    coins.append(nickles)
                for coin in range(int(input("How many pennies?: "))):
                    pennies = Coin("Pennies",0.25)
                    coins.append(pennies)
                print("\nWait a minute!")
                for i in range(10): print(">>", end=""), sleep(0.3)
                for coin in coins:sum_coins += coin.value
                sum_coins = round(sum_coins,2)
                break
            except:
                print("Please insert only coins!")
                continue

        if sum_coins > self.prices[order]:
            self.resources["Money"] += self.prices[order]
            print(f"\nHere is your {sum_coins-self.prices[order]}$ in change")
            return True
        print(f"Sorry that's not enough money. Money refunded! {sum_coins}")
        return False
    def make_coffee(self,order):
        coffee = Coffee(order)
        print(f"\nHere is your {order} ☕ Enjoy!\n")
        input()
        return coffee
    def take_resource(self,order):
        self.resources["Water"] -= self.resources_consume[order]["Water"]
        self.resources["Milk"] -= self.resources_consume[order]["Milk"]
        self.resources["Coffee"] -= self.resources_consume[order]["Coffee"]
        return True

class Main:
    def launch():
        coffeeMachine = CoffeeMachine()
        while True:
            order = coffeeMachine.get_order()
            if order == "off": break
            print("Thank you for your order! Let me check!")
            for i in range(10): print(">>", end=""), sleep(0.3)
            resources = coffeeMachine.check_resources(order)
            if not resources:
                if not coffeeMachine.check_available_coffees(): break
                else:continue
            cash_taken = coffeeMachine.take_cash(order)
            if cash_taken:resources_taken = coffeeMachine.take_resource(order)
            if resources_taken: coffeeMachine.make_coffee(order)
            else: continue

if __name__=="__main__":
    Main.launch()

