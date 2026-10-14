from nutrition import Nutrition
from food import Food
class Meal:
    # A meal is just a combination of foods. It has calories and macros and a list of foods.
    def __init__(self, name, ingredients_and_amounts):
        self.name = name
        self.ingredients_and_amounts = ingredients_and_amounts

    @property
    def nutrition(self):
        return sum((ingredient.nutrition*amount for ingredient, amount in self.ingredients_and_amounts.items()), Nutrition())

    def add_food(self, ingredient, amount):
        '''
        Args:
          ingredient (Food): Food to add to the meal
          amount (int): Amount of food to add
        Adds a food to the meal
        '''
        if ingredient in self.ingredients_and_amounts:
            self.ingredients_and_amounts += amount
        else:
            self.ingredients_and_amounts[ingredient] = amount

    def remove_food(self, ingredient, portion):
        '''
        Args:
          ingredient (Food): Food to remove from the meal
          portion (int): Amount of food to remove
        Remove a portion of food from the meal.
        '''
        if ingredient in self.ingredients_and_amounts and self.ingredients_and_amounts[ingredient]>=portion:
            self.ingredients_and_amounts[ingredient] -=portion
        if self.ingredients_and_amounts[ingredient] == 0:
            self.ingredients_and_amounts.remove(ingredient)

    def __str__(self):
        ans = f"The meal {self.name} consists of:\n"
        for ingredient,amount in self.ingredients_and_amounts.items():
            ans+= ingredient.describe_portion(amount)
        ans += self.nutrition.__str__()
        return ans
    
    def get_macros_for_portion(self, portion = 1):
        '''
        Args:
          portion (int): Amount of portions of that meal
        Return information about macros for a given amount of portions of a meal
        Output:
          (namedtuple) with fields [protein, carbs, fats] 
        '''
        total_protein = 0
        total_carbs = 0
        total_fats = 0
        for ingred, amount in self.ingredients_and_amounts.items():
            ingred_macros = ingred.get_macros_for_portion(amount)
            total_protein += ingred_macros[0]
            total_carbs += ingred_macros[1]
            total_fats += ingred_macros[2]
        return (total_protein*portion, total_carbs*portion, total_fats*portion)
    
    def get_cals_for_portion(self, portion=1 ):
        '''
        Args:
          portion (int): Number of portions
        Return information about the calories for a given amount of portions of the meal
        Output:
          (int) number of calories for that portion
        ''' 
        total_cals = 0
        for ingred, amount in self.ingredients_and_amounts.items():
            total_cals += ingred.get_cals_for_portion(amount)
        return total_cals*portion

    def describe_portion(self, portion = 1):
        '''
        Args:
          portion (int): Number of portions
        Return information as a string about a given amount of portions of the meal
        Output:
          (string) information about the portion portions of the meal.
        '''
        ans = f"{portion} of {self.name} contains:\n"
        for food, amount in self.ingredients_and_amounts.items():
            ans += food.describe_portion(amount*portion)
        return ans
    
if __name__ == '__main__':
    rice = Food('rice', Nutrition(280, 2.7, 50, 0))
    chicken = Food('chicken', Nutrition(150, 30, 4, 5))
    peas = Food('peas', Nutrition(20, 2,1,0))

    meal = Meal('Chicken Rice and Peas', {rice:2, chicken:3, peas:1})
    meal.add_food(Food('Skyr', Nutrition(88, 11,1,3)),.5)
    print(meal)
    print(meal.get_cals_for_portion(2))