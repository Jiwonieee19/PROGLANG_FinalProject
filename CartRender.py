from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

def render_cart(cartFrame, cartItems, cartImageRefs, redPalette):
    """Refresh cart thumbnails inside frame2Bg.

    Each order shows the dish plus chosen add-ons and drink thumbnails.
    """
    for widget in cartFrame.winfo_children():
        widget.destroy()

    cartImageRefs.clear()

    dish_size = (int(110 / 1.8), int(132 / 1.8))  # main dish thumb
    extra_size = (int(70 / 1.8), int(80 / 1.8))   # add-on/drink thumb

    if not cartItems:
        try:
            placeholder_img = Image.open('reso/FinalReso/ICON/default.png')
            placeholder_img = placeholder_img.resize(dish_size, Image.LANCZOS)
            placeholder_photo = ImageTk.PhotoImage(placeholder_img)
            cartImageRefs.append(placeholder_photo)
            ctk.CTkLabel(cartFrame, image=placeholder_photo, text="", fg_color=redPalette).pack(side="left", padx=5)
        except FileNotFoundError:
            pass
        return

    for entry in cartItems:
        # Normalize legacy strings into dict entries
        if isinstance(entry, str):
            order = {"dish": entry, "addOns": [], "drinks": []}
        else:
            order = entry

        order_frame = ctk.CTkFrame(cartFrame, fg_color=redPalette)
        order_frame.pack(side="left", padx=6, pady=4)

        row_frame = ctk.CTkFrame(order_frame, fg_color=redPalette)
        row_frame.pack(side="top")

        # Dish thumbnail
        dish_path = order.get("dish")
        if dish_path:
            try:
                img = Image.open(dish_path)
                img = img.resize(dish_size, Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                cartImageRefs.append(photo)
                ctk.CTkLabel(row_frame, image=photo, text="", fg_color=redPalette).pack(side="left", padx=2)
            except FileNotFoundError:
                pass

        # Extras row (add-ons + drinks) placed to the right to stay within cart height
        # Only pack if there are extras to avoid empty frame taking space
        addons = order.get("addOns", [])
        drinks = order.get("drinks", [])
        
        if addons or drinks:
            extras_frame = ctk.CTkFrame(row_frame, fg_color=redPalette)
            extras_frame.pack(side="left", padx=2)

            def _add_thumb(path):
                if not path:
                    return
                try:
                    img = Image.open(path)
                    img = img.resize(extra_size, Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    cartImageRefs.append(photo)
                    ctk.CTkLabel(extras_frame, image=photo, text="", fg_color=redPalette).pack(side="left", padx=2)
                except FileNotFoundError:
                    pass

            for addon_path in addons:
                _add_thumb(addon_path)

            for drink_path in drinks:
                _add_thumb(drink_path)
