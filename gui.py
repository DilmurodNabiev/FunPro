import main
import FreeSimpleGUI as sg
import webbrowser

layout = [
    [sg.Text("Welcome to FTA")],
    [sg.Button("GitHub Repository", key="-GIT-")],
    [sg.Text("")],
    [sg.Button("Add New Workout")],
    [sg.Button("Delete Workout")],
    [sg.Button("Update Workout")],
    [sg.Button("Show All Workouts")],

]

window = sg.Window("Fitnes Tracker App (FTA)", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == "-GIT-":
        webbrowser.open("https://github.com/DilmurodNabiev/FunPro")

window.close()

