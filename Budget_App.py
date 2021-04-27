class Category:
    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} into the {} category.".format(amount, self.category)

    def budget_balance(self):
        return "Your current balance is: {} ".format(self.amount)

    def check_balance(self, amount):
        # this returns a boolean and checks if the amount is less than or greater than self.amount
        if amount < self.amount:
            return True
        if amount > self.amount:
            return False

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} from the {} category.".format(amount, self.category)

    def transfer(self, amount, category):
        # transfer between two instantiated categories
        self.withdraw(amount) + category.withdraw(amount)
        return "You have successfully transferred {} out of the {} category.".format(amount, self.category)


clothing_category = Category("Clothing", 100)
food_category = Category("Food", 600)
entertainment_category = Category("Entertainment", 400)
car_category = Category("Car Expenses", 300)
rent_category = Category("Rent", 1200)

# print(food_category.withdraw(250))

print(food_category.budget_balance())
print(food_category.transfer(601, rent_category))
print(food_category.check_balance(1))
print(food_category.budget_balance())
