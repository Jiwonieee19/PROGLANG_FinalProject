from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *

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

    label2 = Label(lastPage, text='Please GRAB the RECEIPT', font=('Baloo Tammudu', 18), fg=whitePalette, bg=yellowPalette)
    label2.place(relx=0.5, rely=0.85, anchor='center')

    # Icon grab
    img2 = Image.open('reso/FinalReso/ICON/grab.png')
    grabLogo = img2.resize((135,102))
    grabLogoPhoto = ImageTk.PhotoImage(grabLogo)
    logoLabel = Label(lastPage, image=grabLogoPhoto, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0.93, anchor='center')