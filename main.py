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
img_width, img_height = 600, 600


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb


def change_text_color():
    colors = askcolor(title="Watermark Color Chooser")
    global text_color
    text_color = colors[0]
    color_selection.configure(bg=colors[1])


def apply_watermark():
    watermark_image = Image.open(image).convert('RGBA')
    text_image = Image.new('RGBA', watermark_image.size, (255, 255, 255, 0))

    my_font = ImageFont.truetype(font_var.get(), current_font_size.get())
    my_watermark = ImageDraw.Draw(text_image)

    opacity_tuple = ((round(current_opacity.get() * 2.55)),)
    rgba_text_color = text_color + opacity_tuple

    # Setup Watermark
    my_watermark.text((width_position.get(), height_position.get()),
           watermark_input.get(),
           font=my_font,
           fill=rgba_text_color
           )

    # Combine image with text and save image
    combined = Image.alpha_composite(watermark_image, text_image).convert('RGB')
    combined.save("new_img_with_watermark.jpeg", format='JPEG')

    # Apply changes to screen
    updated_image = ImageTk.PhotoImage(Image.open("new_img_with_watermark.jpeg"))
    label.configure(image=updated_image)
    label.image = updated_image


def file_open():
    global image, img_width, img_height
    image = askopenfilename()   # Add filetypes
    img_width, img_height = Image.open(image).size
    width_position.config(to=img_width)
    height_position.config(to=img_height)
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
current_font_size = IntVar(value=30)
font_size_label = Label(edit_frame, text="Fontsize: ")
font_size_label.grid(column=0, row=3)
font_size = Spinbox(edit_frame, from_=8, to=150, wrap=True, textvariable=current_font_size)
font_size.grid(column=1, row=3)
# Opacity
current_opacity = IntVar(value=100)
opacity_label = Label(edit_frame, text="Opacity")
opacity_label.grid(column=0, row=4)
opacity_spinbox = Spinbox(edit_frame, from_=0, to=100, textvariable=current_opacity, wrap=False)
opacity_spinbox.grid(column=1, row=4)
# Text color
color_selection = Canvas(edit_frame, bg=rgb_to_hex(text_color), width=15, height=15)
color_selection.grid(column=0, row=5)
color_button = Button(edit_frame, text="Text Color", command=change_text_color)
color_button.grid(column=1, row=5, columnspan=1)
# Position
height_label = Label(edit_frame, text="Height")
height_label.grid(column=0, row=6)
height_position = Scale(edit_frame, from_=0, to=img_height, orient=VERTICAL)
height_position.grid(column=1, row=6)
width_label = Label(edit_frame, text="Width")
width_label.grid(column=0, row=7)
width_position = Scale(edit_frame, from_=0, to=img_width, orient=HORIZONTAL)
width_position.grid(column=1, row=7)

# Angle


# Apply Button
confirm_button = Button(edit_frame, text="Add Watermark", command=apply_watermark)
confirm_button.grid(column=0, row=8, columnspan=2)

# save_button
save_button = Button(edit_frame, text="Save", command=save_new_image)
save_button.grid(column=0, row=9, columnspan=2)
window.mainloop()
