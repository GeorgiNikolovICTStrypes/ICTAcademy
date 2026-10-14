
class Nutrition:
    def __init__(self, calories = 0, protein = 0, carbohydrates = 0, fats = 0):
        '''
        Args:
          calories (int): Amount of calories
          protein (int): Amount of protein
          carbohydrates (int): Amount of carbohydrates
          fats (int): Amount of fats
        Creates a Nutrition object with passed nutritional values to represent the nutritional values of food.
        '''
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats

    def __add__(self, nutri2):
        return Nutrition(self.calories + nutri2.calories, self.protein + nutri2.protein, self.carbohydrates + nutri2.carbohydrates, self.fats + nutri2.fats)

    def __mul__(self, portions):
        return Nutrition(self.calories*portions, self.protein*portions, self.carbohydrates*portions, self.fats*portions)

    def __str__(self):
        return f"Calories: {self.calories}kcal\nP - {self.protein}g\nC - {self.carbohydrates}g\nF - {self.fats}g\n"

    def describe_portion(self, portion = 1):
        '''
        Args: 
          portion (int): Number of portions
        return info for the nutrition for a given amount of portions
        Output:
          (string): A string in the format Calories - (cals), P - (protein), C - (carbs), F - (fats)
        '''
        return f"Calories - {round(self.calories*portion,2)}kcal\nP - {round(self.protein*portion,2)}g\nC - {round(self.carbohydrates*portion,2)}g\nF - {round(self.fats*portion,2)}g\n"
    
    def get_macros_for_portion(self, portion = 1):
        '''
        Args:
          portion (int): Number of portions
        Return information about macros for a given amount of portions
        Output:
          (namedtuple) with fields [protein, carbs, fats]
        '''
        return (round(self.protein*portion,2), round(self.carbohydrates*portion,2), round(self.fats*portion,2))
            
    def __eq__(self, other):
        return self.calories == other.calories and self.protein == other.protein and self.carbohydrates == other.carbohydrates and self.fats == other.fats

    def __hash__(self):
        return hash((self.calories, self.protein, self.carbohydrates, self.fats))

    def get_cals_for_portion(self, portion = 1):
        '''
        Args:
          portion (int): Number of portions
        Return information about the calories for a given amount of portions
        Output:
          (int) number of calories for that portion
        '''      
        return round(self.calories*portion,2)
    
if __name__ == '__main__':
    nutri1 = Nutrition(200, 1, 5, 1)
    nutri2 = Nutrition(1023 , 5 ,1 ,1)
    nutri3 = nutri1 + nutri2
    print(nutri3.get_macros_for_portion())
    print(nutri3)