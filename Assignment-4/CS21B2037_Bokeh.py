import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()
window.title('Bokeh Effect Adder')

image_label = tk.Label(window)
image_label.pack()

def insert_img():
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image files", "*.jpg *.png *.gif *.jpeg")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

def bokeh_effect():
    pass

window.geometry('600x600')
insert_btn = tk.Button(window, text="Insert", command=insert_img)
insert_btn.pack()
bokeh_btn = tk.Button(window, text="Bokeh", command=bokeh_effect)
bokeh_btn.pack()

window.mainloop()
