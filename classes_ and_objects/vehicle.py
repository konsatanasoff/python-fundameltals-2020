class Vehicle:
    def __init__(self, type, model, price):
        self.owner = None
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner is not None:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"