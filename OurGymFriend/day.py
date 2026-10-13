from datetime import date
class Day:
    def __init__(self, day = None, calories_goal = 0, protein_goal = 0, carbs_goal = 0, fats_goal = 0):
        self._entries = []
        self.date = day
        self._calories_goal = calories_goal
        self._protein_goal = protein_goal
        self._carbs_goal = carbs_goal
        self._fats_goal = fats_goal

    def add_entry(self, entry):
        self._entries.append(entry)

    def get_info_for_day(self):
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

        res_string = f"Today you hit {day_cals}/{self._daily_calories}. Your macro goals were:\n"
        res_string += f"Protein: {day_protein}/{self._daily_protein}\n"
        res_string += f"Carbs: {day_carbs}/{self._daily_carbs}\n"
        res_string += f"Fats: {day_fats}/{self._daily_fats}\n"

        return res_string

