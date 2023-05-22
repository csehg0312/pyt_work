import PySimpleGUI as sg
import io
from PIL import Image

def open_image():
    # Open the image file
    image_path = "C:/Users/csehg/Pictures/GIF_1.png"  # Replace with the actual image path
    image = Image.open(image_path)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    # Create the PySimpleGUI window
    layout = [
        [sg.Canvas(key="-CANVAS-", size=(700,700))],
        [sg.Button("Exit")]
    ]
    window = sg.Window("Image Canvas", layout, finalize=True)

    # Get the canvas element from the window
    canvas = window["-CANVAS-"].TKCanvas

    # Paint the image onto the canvas
    img = sg.tk.PhotoImage(master=canvas, data=image_bytes.read())
    canvas.create_image(0, 0, anchor="nw", image=img)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break

    window.close()

open_image()
