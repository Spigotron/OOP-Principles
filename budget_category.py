import re

class BudgetCategory():
    def __init__(self, category_name, allocated_budget, remaining_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = remaining_budget

    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category):
        if re.match(r"[A-Za-z_]+", str(new_category)):
            self.__category_name = str(new_category)
        else:
            print(f"Error: invalid category name.")

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, new_budget):
        if re.match(r"[0-9]+", str(new_budget)):
            self.__allocated_budget = int(new_budget)
            self.__remaining_budget = int(new_budget)
        else:
            print(f"Error: invalid format. Please enter only numbers.")

    def add_expense(self, amount):
        if 0 < amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
        elif amount <= 0:
            print(f"Error: amount must be a positive number.")
        elif amount > self.__remaining_budget:
            print(f"Error: amount must be smaller than or equal to budget.")
        else:
            print(f"Error: invalid format. Please enter only numbers.")

    def display_category_summary(self):
        print(f"Category name: {self.__category_name}")
        print(f"Allocated budget: {self.__allocated_budget}")
        print(f"Remaining budget: {self.__remaining_budget}")

category1 = BudgetCategory("entertainment", 1000, 1000)
category2 = BudgetCategory("food", 500, 500)
category3 = BudgetCategory("utilities", 250, 250)

category1.add_expense(250)
category1.display_category_summary()
category2.add_expense(100)
category2.display_category_summary()
category3.add_expense(25)
category3.display_category_summary()