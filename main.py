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
    def add_workout():
        pass

    def to_dict(): # Loades data from JSON and turns it to Dictionary
        pass

    def update():  # Updates the data in JSON databse
        pass

    def display(): # Displays data from databse
        pass



def validation(workout: Workout):
    pass

        
def normilize():
    pass

# def update_workout(workout_id): 
#     pass

# def remove_workout(workout_id):
#     pass

# def view_workouts():
#     pass

# def totals():
#     pass

# def filter(criteria):
#     pass

# def sort(criteria):
#     pass

# date = datetime.datetime.now()

# new_workout = Workout("sdf", date, "squats", "15", 15.5)

# print(add_workout(new_workout))

