# Todo 1: Make file upload work
# Todo 2: Move watermark functionality
# Todo 3: Angle Watermark functionality
# Todo 4: Save final image to selected destination
# Todo 5: Clean up interface
# Todo 6: Watermark opacity
# Todo 7: Add more fonts
# Todo 7: Save favorite watermarks
# Todo 8: Edit multiple photos

from tkinter import *
from tkinter.ttk import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageDraw, ImageFont
from fonts import FONTS


text_color = (0, 0, 0)
image = "duck.jpeg"


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


def show_window():
    uploaded_image = ImageTk.PhotoImage(Image.open(image))
    label.configure(image=uploaded_image)
    label.image = uploaded_image
    window.deiconify()


def file_open():
    global image
    image = askopenfilename()   # Add filetypes
    # remove path info and just show filename
    filename = image.split("/")[-1]
    # Display selected file
    filename_label.config(text=filename)
    # show upload button
    upload_button.pack()


window = Tk()
window.title("Image Watermark")
window.resizable(False, False)
# Hide edit window
window.withdraw()

# Upload file window
upload_window = Toplevel(window)
upload_window.geometry("300x200")
upload_window.title("Upload files")


# Choose file button
choose_file_button = Button(upload_window, text="Choose File", command=file_open)
choose_file_button.pack()
# Display file name between buttons
filename_label = Label(upload_window, text="No file selected")
filename_label.pack()
# Upload button
upload_button = Button(upload_window, text="Upload", command=show_window)

# Image display
img = ImageTk.PhotoImage(Image.open(image))
label = Label(window, image=img)
label.pack(side=LEFT)
label.grid(column=0, row=0, rowspan=5)

# Watermark text
watermark_label = Label(text="Watermark Text: ")
watermark_label.grid(column=1, row=0)
watermark_input = Entry()
watermark_input.grid(column=2, row=0)

# Font
font_label = Label(text="Font: ")
font_label.grid(column=1, row=1)
font_var = StringVar()
# font_var.set("Helvetica")
drop_menu = OptionMenu(window, font_var, FONTS[0], *FONTS)
drop_menu.grid(column=2, row=1)

# font size
current_value = IntVar()
font_size_label = Label(text="Fontsize: ")
font_size_label.grid(column=1, row=2)
font_size = Spinbox(from_=8, to=75, textvariable=current_value, wrap=True)
font_size.grid(column=2, row=2)

# Text color
color_button = Button(window, text="Text Color", command=change_text_color)
color_button.grid(column=1, row=3, columnspan=2)

# Position

# Angle


# Button
confirm_button = Button(text="Add Watermark", command=apply_watermark)
confirm_button.grid(column=2, row=4)


window.mainloop()

