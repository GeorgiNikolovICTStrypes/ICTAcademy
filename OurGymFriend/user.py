from day import Day
class User:
    def __init__(self, name, calorie_goal, protein_goal, carbs_goal = 0, fat_goal = 0):
        self._name = name 
        self.calorie_goal = calorie_goal
        self.protein_goal = protein_goal
        self.carbs_goal = carbs_goal
        self.fat_goal = fat_goal
        self.logs = {}
    
    def add_day(self, day):
         self.logs[day] = Day(day, self.calorie_goal, self.protein_goal, self.carbs_goal, self.fat_goal)

    def add_entry(self, day, entry):
        self.logs[day].add_entry(entry)

    def get_day(self, day):
        return self.logs[day]

    def get_info_for_day(self, day):
        day_obj = self.get_day(day)
        return day_obj.get_info_for_day()

