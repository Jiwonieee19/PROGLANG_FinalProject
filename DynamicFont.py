from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

from scipy.datasets import ascent


def usingOurFont(text, textWidth, fontSize, fontColor):
    # Create custom font image with PIL
    font_path = os.path.abspath("reso/BalooTammudu-Regular.ttf")
    custom_font = ImageFont.truetype(font_path, fontSize)

    # Create image with text
    text_img = Image.new('RGBA', (textWidth, fontSize+10), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 0), text, font=custom_font, fill=fontColor)

    # Convert to PhotoImage
    text_photo = ImageTk.PhotoImage(text_img)
    return text_photo


def usingOurFontWithHeight(text, textWidth, textHeight, fontSize, fontColor, x, y):
    # Create custom font image with PIL
    font_path = os.path.abspath("reso/BalooTammudu-Regular.ttf")
    custom_font = ImageFont.truetype(font_path, fontSize)

    # Create image with text
    text_img = Image.new('RGBA', (textWidth, textHeight), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_img)
    draw.text((x, y), text, font=custom_font, fill=fontColor)

    # Convert to PhotoImage
    text_photo = ImageTk.PhotoImage(text_img)
    return text_photo

def usingOurFontWithPadding(text, textWidth, fontSize, fontColor):

    bottomPadding = 6
    # Create custom font image with PIL
    font_path = os.path.abspath("reso/BalooTammudu-Regular.ttf")
    custom_font = ImageFont.truetype(font_path, fontSize)

    # Create image with text
    text_img = Image.new('RGBA', (textWidth, fontSize+10+bottomPadding), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 0), text, font=custom_font, fill=fontColor)

    # Convert to PhotoImage
    text_photo = ImageTk.PhotoImage(text_img)

    return text_photo
