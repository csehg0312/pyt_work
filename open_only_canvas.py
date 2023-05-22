import PySimpleGUI as sg
from PIL import Image, ImageTk

def open_image():
    # Open the image file
    image_path = "C:/Users/csehg/Pictures/prof.jpg"  # Replace with the actual image path
    image = Image.open(image_path)

    # Create a PySimpleGUI window
    layout = [[sg.Canvas(key="-CANVAS-", size=(700,700))]]
    window = sg.Window("Image Canvas", layout, finalize=True)

    # Convert the image to Tkinter format
    tk_image = ImageTk.PhotoImage(image)

    # Get the canvas element from the window
    canvas = window["-CANVAS-"].TKCanvas

    # Paint the image onto the canvas
    canvas.create_image(0, 0, anchor="nw", image=tk_image)

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

    window.close()

open_image()
