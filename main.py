import os
import json
import datetime

# Fitness Tracker 

class Workout:
    def __init__(self, id: int, date: datetime, name: str, calories: float, duration_min: float):
        self.id = id
        self.date = date
        self.name = name
        self.calories = calories
        self.duration = duration_min

    def __str__(self):
        return(
            f"Workout created:\n"
            f"{"-"*3} ID:{self.id}\n"
            f"{"-"*3} Date:{self.date}\n"
            f"{"-"*3} Name:{self.name}\n"
            f"{"-"*3} Calories:{self.calories}\n"
            f"{"-"*3} Duration(in minutes):{self.duration}\n"
            )

    def to_dict(self): # Loades data from JSON and turns it to Dictionary
        if validation(self) != True:
            return validation(self)
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "name": self.name.casefold().strip(),
            "calories": self.calories,
            "duration": self.duration
        }



def validation(workout: Workout) -> dict | str:
    if not isinstance(workout, Workout):
        return "The function add_workout expects Workout object"

    if not isinstance(workout.date, datetime.datetime):
        return "Workout date must be 'datetime' object"

    try:
        workout.id = int(workout.id)
    except ValueError as e:
        return f"Wrokout ID must be intager. \nError message: {e}"
    
    try:
        workout.calories = float(workout.calories)
    except ValueError as e:
        return f"Wrokout calories must be float or intager. \nError message: {e}"

    try:
        workout.duration = float(workout.duration)
    except ValueError as e:
        return f"Wrokout duration(in mins) must be float or intager. \nError message: {e}"
    
    return True
    
def load_database() -> list:
    if not os.path.exists("workouts_db.json"):
        with open("workouts_db.json", "w") as db_file:
            json.dump([], db_file)

    with open("workouts_db.json", "r") as db_file:
        data = json.load(db_file)
    
    return data

def add_workout(workout: Workout) -> str:
    validation_result = validation(workout)
    if validation_result != True:
        return validation_result

    data = load_database()
    data.append(workout.to_dict())

    with open("workouts_db.json", "w") as db_file:
        json.dump(data, db_file, indent=4)

    return "Workout added successfully."



# Test
date = datetime.datetime.now()

new_workout = Workout("101", date, "squats", "15", 15.5)
new_workou2 = Workout("112", date, "squats", 15, "15.5")


print(add_workout(new_workout))
print(add_workout(new_workou2))


