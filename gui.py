import FreeSimpleGUI as sg
import datetime
from main import (
    Workout,
    add_workout,
    delete_workout,
    update_workout,
    show_all_workouts,
    sort_workouts,
    filter_workouts,
    total_caloriesDuration
)

sg.theme("DarkBlue3")



def popup_result(result):
    sg.popup_scrolled(str(result), title="Result", size=(60, 15))


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

def show_table_window(title: str, data: list):

    if not data:
        sg.popup("No data found.", title=title)
        return

    table_data = [
        [w['id'], w['date'], w['name'], w['calories'], w['duration']]
        for w in data
    ]

    total_cal, total_dur = total_caloriesDuration()
    table_data.append([])
    table_data.append(["Total", "", "", total_cal, total_dur])

    layout = [
        [sg.Text(title, font=("Arial", 14))],
        [sg.Table(
            values=table_data,
            headings=['ID', 'Date', 'Name', 'Calories', 'Duration (min)'],
            auto_size_columns=False,
            col_widths=[8, 20, 20, 12, 12],
            justification="center",
            num_rows=15
        )],
        [sg.Button("Back")]
    ]

    window = sg.Window(title, layout)

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

    window.close()


def add_workout_window():
    layout = [
        [sg.Text("Add Workout", font=("Arial", 14))],
        [sg.Text("ID"), sg.Input(key="ID")],
        [sg.Text("Name"), sg.Input(key="NAME")],
        [sg.Text("Calories"), sg.Input(key="CAL")],
        [sg.Text("Duration (min)"), sg.Input(key="DUR")],
        [sg.Button("Add"), sg.Button("Back")]
    ]

    window = sg.Window("Add Workout", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        if event == "Add":
            try:
                popup_result(add_workout(
                    id=values["ID"],
                    date=datetime.datetime.now(),
                    name=values["NAME"],
                    calories=values["CAL"],
                    duration=values["DUR"]
                ))
            except Exception as e:
                popup_result(e)

    window.close()



def delete_workout_window():
    layout = [
        [sg.Text("Delete Workout", font=("Arial", 14))],
        [sg.Text("Workout ID"), sg.Input(key="ID")],
        [sg.Button("Delete"), sg.Button("Back")]
    ]

    window = sg.Window("Delete Workout", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        if event == "Delete":
            popup_result(delete_workout(int(values["ID"])))

    window.close()


def update_workout_window():
    layout = [
        [sg.Text("Update Workout", font=("Arial", 14))],
        [sg.Text("Existing ID"), sg.Input(key="OLD_ID")],
        [sg.Text("New ID"), sg.Input(key="ID")],
        [sg.Text("Date (YYYY-MM-DD HH:MM:SS)"), sg.Input(key="DATE")],
        [sg.Text("Name"), sg.Input(key="NAME")],
        [sg.Text("Calories"), sg.Input(key="CAL")],
        [sg.Text("Duration (min)"), sg.Input(key="DUR")],
        [sg.Button("Update"), sg.Button("Back")]
    ]

    window = sg.Window("Update Workout", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        if event == "Update":
            try:
                workout = Workout(
                    id=int(values["ID"]),
                    date=parse_date(values["DATE"]),
                    name=values["NAME"],
                    calories=float(values["CAL"]),
                    duration_min=float(values["DUR"])
                )
                popup_result(update_workout(int(values["OLD_ID"]), workout))
            except Exception as e:
                popup_result(e)

    window.close()

def show_workouts_window():
    data = show_all_workouts()
    show_table_window("All Workouts", data)

def sort_workouts_window():
    layout = [
        [sg.Text("Sort Workouts", font=("Arial", 14))],
        [sg.Text("Key (id / date / name / calories / duration)")],
        [sg.Input(key="KEY")],
        [sg.Button("Sort"), sg.Button("Back")]
    ]

    window = sg.Window("Sort Workouts", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        if event == "Sort":
            try:
                data = sort_workouts(values["KEY"])
                show_table_window("Sorted Workouts", data)
            except Exception as e:
                popup_result(e)

    window.close()


def filter_workouts_window():
    layout = [
        [sg.Text("Filter Workouts", font=("Arial", 14))],
        [sg.Text("Key"), sg.Input(key="KEY")],
        [sg.Text("Value"), sg.Input(key="VALUE")],
        [sg.Button("Filter"), sg.Button("Back")]
    ]

    window = sg.Window("Filter Workouts", layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Back"):
            break

        if event == "Filter":
            try:
                data = filter_workouts((values["COLUMN NAME"], values["VALUE"]))
                show_table_window("Filtered Workouts", data)
            except Exception as e:
                popup_result(e)

    window.close()



def main_menu():
    layout = [
        [sg.Text("Fitness Tracker", font=("Arial", 18), justification="center")],
        [sg.Text("GitHub", font=("Arial", 12), key="GITHUB_LINK", text_color="blue", enable_events=True)],
        [sg.HorizontalSeparator()],
        [sg.Button("Add Workout")],
        [sg.Button("Delete Workout")],
        [sg.Button("Update Workout")],
        [sg.Button("Show All Workouts")],
        [sg.Button("Sort Workouts")],
        [sg.Button("Filter Workouts")],
    ]

    window = sg.Window("Main Menu", layout, size=(300, 350))

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

        if event == "Add Workout":
            add_workout_window()
        elif event == "Delete Workout":
            delete_workout_window()
        elif event == "Update Workout":
            update_workout_window()
        elif event == "Show All Workouts":
            show_workouts_window()
        elif event == "Sort Workouts":
            sort_workouts_window()
        elif event == "Filter Workouts":
            filter_workouts_window()
        elif event == "GITHUB_LINK":
            sg.webbrowser.open("https://github.com/DilmurodNabiev/FunPro")

    window.close()


if __name__ == "__main__":
    main_menu()
