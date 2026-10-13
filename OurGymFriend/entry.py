from food import Food
from meal import Meal
from nutrition import Nutrition
class Entry:
    def __init__(self, label, foods_and_meals = {}):
        self.label = label
        self.foods_and_meals = foods_and_meals

    def total_calories(self):
        total = 0
        for food, portion in self.foods_and_meals.items():
            total += food.get_cals_for_portion(portion)
        return total

    def add_to_entry(self, item, portion):
        if item in self.foods_and_meals:
            self.foods_and_meals[item]+=portion
        else: 
            self.foods_and_meals[item] = portion

    def remove_entry(self, item, portion):
        if item in self.foods_and_meals and self.foods_and_meals[item]>=portion:
            self.foods_and_meals[item] -=portion
        if self.foods_and_meals[item] == 0:
            self.foods_and_meals.remove(item)

    def __str__(self):
        ans = f"{self.label}\n===========\n"
        for item, amount in self.foods_and_meals.items():
            ans += item.describe_portion(amount)
        return ans

    def total_calories(self):
        total = 0
        for item, portion in self.foods_and_meals.items():
            print(portion)
            
            total += item.get_cals_for_portion(portion)
        return total
    
    def total_macros(self):
        total_protein = 0 
        total_carbs = 0
        total_fats = 0
        for item, portion in self.foods_and_meals.items():
            item_macros = item.get_macros_for_portion(portion)
            total_protein += item_macros[0]
            total_carbs += item_macros[1]
            total_fats += item_macros[2]
        return (total_protein, total_carbs, total_fats)
    
lunch = Entry('Lunch')
lunch.add_to_entry(Food('pudding',nutrition=Nutrition(200,1,4,5)),5)
rice = Food('rice', Nutrition(280, 2.7, 50, 0))
chicken = Food('chicken', Nutrition(150, 30, 4, 5))
peas = Food('peas', Nutrition(20, 2,1,0))

meal = Meal('Chicken Rice and Peas', {rice:2, chicken:3, peas:1})
meal.add_food(Food('Skyr', Nutrition(88, 11,1,3)),.5)
lunch.add_to_entry(meal, 2)
lunch.add_to_entry(Food('black sludge',nutrition=Nutrition(2121,1,4,5)),1)
print(lunch)
print("TOTAL CALS: ", lunch.total_calories())
print("TOTAL MACROS: ", lunch.total_macros())
