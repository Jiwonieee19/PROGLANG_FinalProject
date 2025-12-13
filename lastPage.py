from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *
import sys, os

def LastPage (reviewOrderPage, lastPage): #(unsa e close, unsa e open, unsa e next sa button)

    global grabLogoPhoto, midLogo

    reviewOrderPage.pack_forget()
    lastPage.pack(fill="both", expand=True)
    lastPage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    whitePalette = "#FFFFFF"

    # Logo
    img = Image.open('reso/landingLogo.png')
    reImg = img.resize((221,229))
    midLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(lastPage, image=midLogo, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0.3, anchor='center')

    label = Label(lastPage, text='"Please pay at the counter, THANK YOU."', font=('Baloo Tammudu', 18), fg=whitePalette, bg=yellowPalette)
    label.place(relx=0.5, rely=0.48, anchor='center')

    label1 = Label(lastPage, text='"Going BACK on MAIN PAGE in 5 seconds"', font=('Baloo Tammudu', 18), fg=whitePalette, bg=yellowPalette)
    label1.place(relx=0.5, rely=0.52, anchor='center')

    # Countdown from 5 to 1 and then return to main page
    def update_countdown(seconds):
        try:
            label1.config(text=f'"Going BACK on MAIN PAGE in {seconds} seconds"')
        except Exception:
            pass
        if seconds > 1:
            lastPage.after(1000, lambda: update_countdown(seconds - 1))
        else:
            # Final tick shows 1, then navigate after 1s
            lastPage.after(1000, go_home)

    def go_home():
        # Try returning to initial landing by restarting the app reliably
        try:
            root = lastPage.winfo_toplevel()
            # cleanly destroy current UI before exec
            try:
                root.destroy()
            except Exception:
                pass
            # Relaunch Main.py (absolute path for Windows)
            script_path = os.path.join(os.path.dirname(__file__), 'Main.py')
            os.execl(sys.executable, sys.executable, script_path)
        except Exception:
            # Fallback: just hide last page
            try:
                lastPage.pack_forget()
            except Exception:
                pass

    label2 = Label(lastPage, text='Please GRAB the RECEIPT', font=('Baloo Tammudu', 18), fg=whitePalette, bg=yellowPalette)
    label2.place(relx=0.5, rely=0.85, anchor='center')

    # Icon grab
    img2 = Image.open('reso/FinalReso/ICON/grab.png')
    grabLogo = img2.resize((135,102))
    grabLogoPhoto = ImageTk.PhotoImage(grabLogo)
    logoLabel = Label(lastPage, image=grabLogoPhoto, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0.93, anchor='center')

    # Start the countdown
    update_countdown(5)