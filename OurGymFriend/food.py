from nutrition import Nutrition

class Food:
    def __init__(self, name, nutrition):
        '''
        Args:
          name (string): Name of the food
          nutrition (Nutrition): Nutrition object to represent the nutritional values of the food
        Creates a food object with the passed name and nutrition
        '''
        self.name = name
        self.nutrition = nutrition

    def __str__(self):
        return f"{self.name} which has {self.nutrition.calories}kcal per 100g.\nThe macros per 100g are: P - {self.nutrition.protein}g, C - {self.nutrition.carbohydrates}g, F - {self.nutrition.fats}g\n"

    def get_macros_for_portion(self, portion = 1):
        '''
        Args:
          portion (int): Number of portions
        Return information about macros for a given amount of portions
        Output:
          (namedtuple) with fields [protein, carbs, fats]
        '''
        return self.nutrition.get_macros_for_portion(portion)

    def describe_portion(self, portion = 1):
        '''
        Args: 
          portion (int): Number of portions
        return info for the nutrition for a given amount of portions
        Output:
          (string): A string in the format Info for (meal name)\nCalories - (cals), P - (protein), C - (carbs), F - (fats)
        '''
        return f"Info for {round(100*portion)}g of {self.name}:\n" + self.nutrition.describe_portion(portion)

    def describe_portion_in_grams(self, grams = 100):
        '''
        Args: 
          grams (int): Number of grams
        return info for the nutrition for a given amount of portions
        Output:
          (string): A string in the format Info for (grams) (meal name)\nCalories - (cals), P - (protein), C - (carbs), F - (fats)
        '''
        return f"Info for {grams}g of {self.name}:\n" + self.nutrition.describe_portion(round(grams/100,2))

    def get_cals_for_portion(self, portion):
        '''
        Args:
          portion (int): Number of portions
        Return information about the calories for a given amount of portions
        Output:
          (int) number of calories for that portion
        '''   
        return self.nutrition.get_cals_for_portion(portion)
    
if __name__ == '__main__':

    rice = Food('rice', Nutrition(280, 2.7, 50, 0))
    print(rice.get_macros_for_portion(2))
