# Todo 1: Make file upload work ✔︎
# Todo 2: Move watermark functionality
# Todo 3: Angle Watermark functionality
# Todo 4: Save final image to selected destination ✔︎
# Todo 5: Clean up interface
# Todo 6: Watermark opacity
# Todo 7: Add more fonts
# Todo 7: Save favorite watermarks
# Todo 8: Edit multiple photos

from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont
from fonts import FONTS


text_color = (0, 0, 0)
image = "image_placeholder.jpeg"


def change_text_color():
    colors = askcolor(title="Watermark Color Chooser")
    global text_color
    text_color = colors[0]


def apply_watermark():
    watermark_image = Image.open(image)
    my_font = ImageFont.truetype(font_var.get(), current_value.get())
    edited_image = ImageDraw.Draw(watermark_image)
    edited_image.text((28, 36), watermark_input.get(), font=my_font, fill=text_color)

    # Save image
    watermark_image.save("new_img_with_watermark.jpeg")

    # Apply changes to screen
    updated_image = ImageTk.PhotoImage(Image.open("new_img_with_watermark.jpeg"))
    label.configure(image=updated_image)
    label.image = updated_image


def file_open():
    global image
    image = askopenfilename()   # Add filetypes
    uploaded_image = ImageTk.PhotoImage(Image.open(image))
    label.configure(image=uploaded_image)
    label.image = uploaded_image


def save_new_image():
    global image
    new_image = Image.open("new_img_with_watermark.jpeg")
    file = asksaveasfilename(title="Save Image", filetypes=[("jpeg files", "*.jpg")])

    if file:
        new_image.save(file)


window = Tk()
window.title("Image Watermark")
window.resizable(False, False)

# Image frame
image_frame = Frame(window)
image_frame.grid(column=0, row=0, padx=10, pady=10)

# Image display
img = ImageTk.PhotoImage(Image.open(image))
label = Label(image_frame, image=img)
label.grid(column=0, row=0)

# edit_frame
edit_frame = Frame(window)
edit_frame.grid(column=1, row=0, padx=10, pady=10)

# file upload button
upload_button = Button(edit_frame, text="Upload Image", command=file_open)
upload_button.grid(column=0, row=0, columnspan=2)

# Watermark text
watermark_label = Label(edit_frame, text="Watermark Text: ")
watermark_label.grid(column=0, row=1)
watermark_input = Entry(edit_frame)
watermark_input.grid(column=1, row=1)

# Font
font_label = Label(edit_frame, text="Font: ")
font_label.grid(column=0, row=2)
font_var = StringVar()
drop_menu = OptionMenu(edit_frame, font_var, FONTS[0], *FONTS)
drop_menu.grid(column=1, row=2)

# font size
current_value = IntVar()
font_size_label = Label(edit_frame, text="Fontsize: ")
font_size_label.grid(column=0, row=3)
font_size = Spinbox(edit_frame, from_=8, to=75, textvariable=current_value, wrap=True)
font_size.grid(column=1, row=3)

# Text color
color_button = Button(edit_frame, text="Text Color", command=change_text_color)
color_button.grid(column=0, row=4, columnspan=2)

# Position

# Angle


# Apply Button
confirm_button = Button(edit_frame, text="Add Watermark", command=apply_watermark)
confirm_button.grid(column=0, row=5, columnspan=2)

# save_button
save_button = Button(edit_frame, text="Save", command=save_new_image)
save_button.grid(column=0, row=6, columnspan=2)
window.mainloop()
