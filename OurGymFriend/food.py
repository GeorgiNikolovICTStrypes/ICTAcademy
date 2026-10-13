from nutrition import Nutrition

class Food:
    def __init__(self, name, nutrition):
        self.name = name
        self.nutrition = nutrition

    def __str__(self):
        return f"{self.name} which has {self.nutrition.calories}kcal per 100g.\nThe macros per 100g are: P - {self.nutrition.protein}g, C - {self.nutrition.carbohydrates}g, F - {self.nutrition.fats}g\n"

    def get_macros_for_portion(self, portion = 1):
        return self.nutrition.get_macros_for_portion(portion)

    def describe_portion(self, portions):
        return f"Info for {round(100*portions)}g of {self.name}:\n" + self.nutrition.describe_portion(portions)

    def describe_portion_in_grams(self, grams):
        return f"Info for {grams}g of {self.name}:\n" + self.nutrition.describe_portion(round(grams/100,2))

    def get_cals_for_portion(self, portion):
        return self.nutrition.get_cals_for_portion(portion)
    
if __name__ == '__main__':

    rice = Food('rice', Nutrition(280, 2.7, 50, 0))
    print(rice.get_macros_for_portion(2))
