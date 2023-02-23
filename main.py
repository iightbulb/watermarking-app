from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
import os

BLACK = "#000000"
CREAM = "#FFE6E6"
FONT_NAME = "Courier"

window = Tk()
window.title("Watermark an image")
window.config(padx=60, pady=40, bg=CREAM)
canvas = Canvas(width=200, height=224, bg=CREAM, highlightthickness=0)
fg=BLACK


def add_watermark():
    filepath = filedialog.askopenfilename(title="Open an Image",
                                          filetypes=(("image files", "*.png *.jpg *.RAW "), ("all files", "*.*")))
    im = Image.open(filepath)
    filename = os.path.basename(filepath)
    watermark_image = im.copy()
    draw = ImageDraw.Draw(watermark_image)
    w, h = im.size
    x, y = int(w/2), int(h/2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x

    # prompt user for specified watermark
    watermark_text = input("Type your watermark: ")

    # determine font and fontsize of watermark
    font = ImageFont.truetype('arial.ttf', int(font_size / 6))

    # draw watermark onto image
    draw.text((x, y), watermark_text, fill=(0, 0, 0), font=font, anchor='ms')

    watermark_image.show()
    watermark_image.save(f'watermark-{filename}')


# choose photo button
button1 = Button(text="Choose a photo to watermark", highlightthickness=0, command=add_watermark)
button1.grid(column=0, row=2)


window.mainloop()

