import hashlib
import hmac
import os
from datetime import date
from day import Day
from entry import Entry
from food import Food 
from meal import Meal
from nutrition import Nutrition

class User:
    def __init__(self, name,password, calorie_goal = 0, protein_goal = 0, carbs_goal = 0, fat_goal = 0):
        '''
        Args:
          name (string): Name of the user
          password (string): Password of the user
          calorie_goal (int): Current caloric intake goal
          protein_goal (int): Current protein intake goal
          carbs_goal (int): Current carbs intake goal
          fat_goal (int): Current fats intake goal
        Create a user object with an empty logs dict with key, value pairs of sort (date, Day obj).
        '''
        self._name = name 
        self._salt = os.urandom(16) # generate 16 random bytes unique to this user instance
        self._password_hash = self._hash(password,self._salt)
        self.calorie_goal = calorie_goal
        self.protein_goal = protein_goal
        self.carbs_goal = carbs_goal
        self.fat_goal = fat_goal
        self.logs = {}
    
    def add_day(self, day):
         '''
         Args:
           day (datetime): Day to add logs for
         Add a day to the logs dict
         '''
         self.logs[day] = Day(day, self.calorie_goal, self.protein_goal, self.carbs_goal, self.fat_goal)

    def add_entry(self, day, entry):
        '''
        Args:
          day (datetime): Day to add logs for
          entry (Entry): Entry to add to the day.
        Adds an entry to a logged day. 
        '''
        if day not in self.logs:
            self.add_day(day)
        self.logs[day].add_entry(entry)

    def get_day(self, day):
        '''
        Args:
          (datetime) day to find the logs for.
        Returns the logs for that day
        Output:
          (day) day object for passed day
        '''
        return self.logs[day]

    def get_info_for_day(self, day):
        '''
        Args:
          (datetime) day to get info for
        Returns info for passed day
        Output:
          (string) With info about the day
        '''
        day_obj = self.get_day(day)
        return day_obj.get_info_for_day()
    @staticmethod
    def _hash(password, salt):
        # arguemnts are algorithm, password (turnt to bytes) salt which is a small string to be added to the password for more secure hasihing
        # And number of iterations (we has it 200,000 times)
        return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200_000)
    def check_password(self, password):
        # we attempt to hash the passed password if they match 
        # return true else return false
        attempt = self._hash(password, self._salt)
        # compare_digest uses the same time for every comparison since == stops at the first
        # difference it could leak data.
        return hmac.compare_digest(attempt, self._password_hash)


if __name__ == '__main__':
    user = User('Geg Ata', 'fashionkilla',3500,220,480,80)
    print(user.check_password('fashionkilla'))
    print(user.check_password('fashionkiller'))
    today = date.today()
    lunch = Entry('Lunch')
    lunch.add_to_entry(Food('pudding',nutrition=Nutrition(200,1,4,5)),5)
    rice = Food('rice', Nutrition(280, 2.7, 50, 0))
    chicken = Food('chicken', Nutrition(150, 30, 4, 5))
    peas = Food('peas', Nutrition(20, 2,1,0))

    meal = Meal('Chicken Rice and Peas', {rice:2, chicken:3, peas:1})
    black_sludge = Food('black sludge',nutrition=Nutrition(2121,1,4,5))
    meal.add_food(Food('Skyr', Nutrition(88, 11,1,3)),.5)
    lunch.add_to_entry(meal, 2)
    lunch.add_to_entry(black_sludge,1)
    lunch.remove_from_entry(black_sludge,1)
    user.add_day(date.today())
    user.add_entry(today, lunch)
    print(user.get_info_for_day(today))
    