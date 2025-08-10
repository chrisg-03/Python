import json
import os

class Machine:
    def __init__(self):
        self.info = "v2/info.json"
        self.load_state()

    def load_state(self):
        if os.path.exists(self.info):
            with open(self.info, "r") as f:
                data = json.load(f)
                self.water = data["water"]
                self.milk = data["milk"]
                self.coffee = data["coffee"]
                self.cash = data["cash"]
        else:
            self.water = 500
            self.milk = 500
            self.coffee = 200
            self.cash = 0.0


    def save_state(self):
        with open(self.info, "w") as f:
            json.dump({
                "water" : self.water,
                "milk" : self.milk,
                "coffee" : self.coffee,
                "cash" : self.cash
            }, f)

    def report(self):
        return (f"Water level: {self.water}ml\n"
                f"Milk level: {self.milk}ml\n"
                f"Coffee level: {self.coffee}g\n"
                f"Cash: {self.cash:.2f}")
    
    def process_order(self, drink_name, drink_data):
        ingredients = drink_data["ingredients"]
        cost = drink_data["cost"]

        if self.water < ingredients.get("water", 0):
            return "Sorry, not enough water"
        
        if self.milk < ingredients.get("milk", 0):
            return "Sorry, not enough milk"
        
        if self.coffee < ingredients.get("coffee", 0):
            return "Sorry, not enough coffee"
        

        try:
            payment = float(input(f"Please insert ${cost}: "))
        except ValueError:
            return "Invalid payment"
        
        if payment < cost:
            return "Not enough money, money refunded"
        
        self.water -= ingredients.get("water", 0)
        self.milk -= ingredients.get("milk", 0)
        self.coffee -= ingredients.get("coffee", 0)
        self.cash += cost

        self.save_state()

        change = payment - cost
        return f"Here is your {drink_name}, Chage: {change:.2f}"        
        
    
class Orders:
    def __init__(self, machine):
        self.machine = machine
        self.menu_items = {
            "espresso": {"ingredients": {"water": 50, "coffee": 10}, "cost": 8.0},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 12.0},
            "cuppuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 11.0}
        }
    
    def take_order(self):
        while True:
            choice = input(f"What would you like? (espresso/latte/cuppuccino/report/off): ").lower()

            if choice == "off":
                print("Energy saving..")
                self.machine.save_state()
                break
            elif choice == "report":
                print(self.machine.report())
            elif choice in self.menu_items:
                result = self.machine.process_order(choice, self.menu_items[choice])
                print(result)
            else:
                print("Invalid choice. Try again")


if __name__ == "__main__":
    machine = Machine()
    orders = Orders(machine)
    orders.take_order()
