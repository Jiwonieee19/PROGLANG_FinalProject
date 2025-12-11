from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

def render_cart(cart_frame, cart_items, cart_image_refs, redPalette):
    """Refresh cart thumbnails inside frame2Bg."""
    for widget in cart_frame.winfo_children():
        widget.destroy()

    cart_image_refs.clear()

    thumb_size = (int(110 / 1.8), int(132 / 1.8))  # downscale from menu images

    if not cart_items:
        try:
            placeholder_img = Image.open('reso/FinalReso/ICON/default.png')
            placeholder_img = placeholder_img.resize(thumb_size, Image.LANCZOS)
            placeholder_photo = ImageTk.PhotoImage(placeholder_img)
            cart_image_refs.append(placeholder_photo)
            ctk.CTkLabel(cart_frame, image=placeholder_photo, text="", fg_color=redPalette).pack(side="left", padx=5)
        except FileNotFoundError:
            pass
        return

    for img_path in cart_items:
        try:
            img = Image.open(img_path)
            img = img.resize(thumb_size, Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            cart_image_refs.append(photo)

            thumb = ctk.CTkLabel(cart_frame, image=photo, text="", fg_color=redPalette)
            thumb.pack(side="left", padx=5)
        except FileNotFoundError:
            continue
