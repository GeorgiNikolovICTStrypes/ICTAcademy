from datetime import date
class Day:
    def __init__(self, day = None, calories_goal = 0, protein_goal = 0, carbs_goal = 0, fats_goal = 0):
        '''
        Args:
          calories_goal (int): caloric goal for the day
          protein_goal (int): protein goal for the day
          carbs goal (int): carbohydrate goal for the day
          fats goal (int): fats goal for the day
        Create a Day object. It has a list of entries, a date and caloric and macro goals.
        '''
        self._entries = []
        self.date = day
        self._calories_goal = calories_goal
        self._protein_goal = protein_goal
        self._carbs_goal = carbs_goal
        self._fats_goal = fats_goal

    def add_entry(self, entry):
        '''
        entry (Entry): entry to add to the Day.
        Adds an entry to the day
        '''
        self._entries.append(entry)

    def get_info_for_day(self):
        '''
        Retruns a string with information about how much of the goals are hit.
        Output:
          (string) Information about the day.
        '''
        day_cals = 0
        day_protein = 0
        day_carbs = 0 
        day_fats = 0
        for entry in self._entries:
            day_cals+=entry.total_calories()
            macros = entry.total_macros()
            day_protein += macros[0]
            day_carbs += macros[1]
            day_fats += macros[2]

        res_string = f"Today you hit {day_cals}/{self._calories_goal}. Your macro goals were:\n"
        res_string += f"Protein: {day_protein}/{self._protein_goal}\n"
        res_string += f"Carbs: {day_carbs}/{self._carbs_goal}\n"
        res_string += f"Fats: {day_fats}/{self._fats_goal}\n"

        return res_string
