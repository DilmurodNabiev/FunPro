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
            return (
                f"Workout created:\n"
                f"--- ID: {self.id}\n"
                f"--- Date: {self.date}\n"
                f"--- Name: {self.name}\n"
                f"--- Calories: {self.calories}\n"
                f"--- Duration (minutes): {self.duration}\n"
            )


    def to_dict(self): # Loades data from JSON and turns it to Dictionary
        if type(validation(self.id, self.date, self.name, self.calories, self.duration)) == str:
            return validation(self.id, self.date, self.name, self.calories, self.duration)
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "name": self.name.casefold().strip(),
            "calories": self.calories,
            "duration": self.duration
        }

obj = Workout(1, datetime.datetime.now(), "Running", 300, 30)

print(obj)

def validation(id, date, name, calories, duration) -> dict | str:

    if not isinstance(date, datetime.datetime):
        return "Workout date must be 'datetime' object"

    try:
        id = int(id)
    except ValueError as e:
        return f"Wrokout ID must be intager. \nError message: {e}"
    
    try:
        calories = float(calories)
    except ValueError as e:
        return f"Wrokout calories must be float or intager. \nError message: {e}"

    try:
        duration = float(duration)
    except ValueError as e:
        return f"Wrokout duration(in mins) must be float or intager. \nError message: {e}"
    
    return {
        "id": id,
        "date": date,
        "name": name.casefold().strip(),
        "calories": calories,
        "duration": duration
    }
    
def load_database() -> list:
    if not os.path.exists("workouts_db.json"):
        with open("workouts_db.json", "w") as db_file:
            json.dump([], db_file)

    with open("workouts_db.json", "r") as db_file:
        data = json.load(db_file)
    
    return data

def is_workout_id_exists(workout_id: int) -> bool:
    data = load_database()
    for workout in data:
        if workout["id"] == workout_id:
            return True
    return False

def add_workout(id: int, date: datetime, name: str, calories: float, duration: float) -> str:
    validation_result = validation(id, date, name, calories, duration)
    if is_workout_id_exists(validation_result["id"]):
        return "Workout ID already exists. Please use a unique ID."
    data = load_database()
    data.append(Workout(validation_result["id"], validation_result["date"], validation_result["name"], validation_result["calories"], validation_result["duration"]).to_dict())

    with open("workouts_db.json", "w") as db_file:
        json.dump(data, db_file, indent=4)

    return "Workout added successfully."

def delete_workout(workout_id: int) -> str:
    data = load_database()
    new_data = [workout for workout in data if workout["id"] != workout_id]

    if len(data) == len(new_data):
        return "Workout ID not found."

    with open("workouts_db.json", "w") as db_file:
        json.dump(new_data, db_file, indent=4)

    return "Workout deleted successfully."


def update_workout(workout_id: int, updated_workout: Workout) -> str:
    validation_result = validation(updated_workout.id, updated_workout.date, updated_workout.name, updated_workout.calories, updated_workout.duration)
    if validation_result != True:
        return validation_result

    data = load_database()
    for index, workout in enumerate(data):
        if workout["id"] == workout_id:
            data[index] = updated_workout.to_dict()
            with open("workouts_db.json", "w") as db_file:
                json.dump(data, db_file, indent=4)
            return "Workout updated successfully."

    return "Workout ID not found."

def show_all_workouts() -> list:
    data = load_database()
    return data 

def sort_workouts(key) -> list:
    data = load_database()
    try:
        sorted_data = sorted(data, key=lambda x: x[key])
        return sorted_data
    except KeyError:
        return f"Invalid key: {key}."
    
def filter_workouts(filtering_obj) -> list:  
    data = load_database()
    key, value = filtering_obj
    filtered_data = [workout for workout in data if str(workout.get(key, "")).casefold() == str(value).casefold()]
    return filtered_data

if __name__ == "__main__":
    # Example usage
    print(add_workout(1, datetime.datetime.now(), "Running", 300, 30))
    print(add_workout(2, datetime.datetime.now(), "Cycling", 250, 45))
    print(show_all_workouts())
    print(sort_workouts("calories"))
    print(filter_workouts(("name", "running")))
    print(delete_workout(1))
    print(show_all_workouts())