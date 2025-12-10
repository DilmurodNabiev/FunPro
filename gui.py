import main
import FreeSimpleGUI as sg

layout = [
    [sg.Text("Welcome to FTA")],
    [sg.Text("GitHub: https://github.com/DilmurodNabiev/FunPro")],
    [sg.Text("")]
]

window = sg.Window("Fitnes Tracker App (FTA)", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()