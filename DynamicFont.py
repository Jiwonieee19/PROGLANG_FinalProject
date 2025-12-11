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

def usingOurFontWithIcon(text, textWidth, fontSize, fontColor, iconPath=None, iconSize=(30, 30)):
    bottomPadding = 6

    # Load custom font
    font_path = os.path.abspath("reso/BalooTammudu-Regular.ttf")
    custom_font = ImageFont.truetype(font_path, fontSize)

    # Prepare text drawing
    text_img = Image.new("RGBA", (textWidth, fontSize + 10 + bottomPadding), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_img)
    draw.text((0, 0), text, font=custom_font, fill=fontColor)

    # If no icon provided, return only text image
    if iconPath is None:
        return ImageTk.PhotoImage(text_img)

    # Load icon
    icon = Image.open(iconPath).convert("RGBA")
    icon = icon.resize(iconSize, Image.Resampling.LANCZOS)

    # Combine icon + text into one image
    total_width = iconSize[0] + 10 + textWidth
    final_height = max(text_img.height, iconSize[1])

    final_img = Image.new("RGBA", (total_width, final_height), (0, 0, 0, 0))

    # Paste icon
    final_img.paste(icon, (0, (final_height - iconSize[1]) // 2), icon)

    # Paste text image
    final_img.paste(text_img, (iconSize[0] + 10, (final_height - text_img.height) // 2), text_img)

    return ImageTk.PhotoImage(final_img)

