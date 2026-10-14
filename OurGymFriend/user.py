import hashlib
import os
from day import Day

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
        self._salt = os.urandom(16)
        self._password_hash = password # since im working only in vanilla python im not hashing the password as its a small project
        # if i wanted to hash it i would use bcrypt.
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
        return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 200_000)
    def check_password(self, password):
        attempt = self._hash(password, self._salt)
