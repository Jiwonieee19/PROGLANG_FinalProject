from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *

def ReviewOrderPage (menuPage, reviewOrderPage, lastPage): #(unsa e close, unsa e open, unsa e next sa button)

    menuPage.pack_forget()
    reviewOrderPage.pack(fill="both", expand=True)
    reviewOrderPage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    global reviewTopRightLogo, ReviewBg, reviewText, BgYellow

    def goBack():
        reviewOrderPage.pack_forget()
        menuPage.pack(fill="both", expand=True)

    # Real Logo top right
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    reviewTopRightLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(reviewOrderPage, image=reviewTopRightLogo, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0, anchor='n')

    # top red bg
    ReviewBg = ctk.CTkFrame(reviewOrderPage, width=475, height=750, corner_radius=10, fg_color=redPalette)
    ReviewBg.place(relx=0.5, rely=0.52, anchor='center')

    reviewText = usingOurFont('REVIEW YOUR ORDER', 370, 38, whitePalette)
    # Create label with the text image
    labelChoice = Label(reviewOrderPage, image=reviewText, bg=redPalette)
    labelChoice.place(relx=0.5, rely=0.161, anchor='center')



    # The Frame for Every order
    BgYellowImg = Image.open('reso/FinalReso/MakeChoiceBG.png')
    reBgYellowImg = BgYellowImg.resize((455,212))
    BgYellow = ImageTk.PhotoImage(reBgYellowImg)
    BgYellowLabel = Label(reviewOrderPage, image=BgYellow, bg=redPalette)
    BgYellowLabel.place(relx=0.5, rely=0.554, anchor='center')



    backPhoto = usingOurFontWithIcon('BACK', 58, 23, whitePalette, iconPath='reso/FinalReso/ICON/return.png', iconSize=(25, 25))
    # back button
    backButton = ctk.CTkButton(reviewOrderPage, width=225, height=50, image=backPhoto, text="", corner_radius=10, fg_color=redPalette, command=lambda: goBack())
    backButton.place(relx=0.27, rely=0.95, anchor='center')

    checkoutPhoto = usingOurFontWithIcon('CHECKOUT', 114, 23, whitePalette, iconPath='reso/FinalReso/ICON/checkout.png', iconSize=(25, 25))
    # checkout button
    checkoutButton = ctk.CTkButton(reviewOrderPage, width=225, height=50, image=checkoutPhoto, text="", corner_radius=10, fg_color=greenButton)
    checkoutButton.place(relx=0.732, rely=0.95, anchor='center')