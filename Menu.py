from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from DynamicFont import *
from OrderType import *

def MenuPage(orderTypePage, menuPage):
    orderTypePage.pack_forget()
    menuPage.pack(fill="both", expand=True)
    menuPage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    global topRightLogo

    def goBack():
        menuPage.pack_forget()      # hide current page
        orderTypePage.pack(fill="both", expand=True)  # show previous page

    # sections = ['Ramen', 'Donburi', 'Others']

    # btnRamen = Button(menuPage, text="RAMEN", font=('Baloo Tammudu', 45))
    # btnDonburi = Button(menuPage, text="DONBURI", font=('Baloo Tammudu', 45))
    # btnOthers = Button(menuPage, text="OTHERS", font=('Baloo Tammudu', 45))

    text_photo = usingOurFontWithPadding('RETURN', 92, 25, whitePalette)
    # return button
    returnButton = ctk.CTkButton(menuPage, width=200, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette, command=goBack)
    returnButton.place(relx=0.25, rely=0.07, anchor='center')

    # Real Logo top right
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    topRightLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(menuPage, image=topRightLogo, bg=yellowPalette)
    logoLabel.place(relx=0.835, rely=0, anchor='n')


    # top red bg
    topBg = ctk.CTkFrame(menuPage, width=475, height=570, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.44, anchor='center')

    ramenText = usingOurFont('RAMEN SECTION', 280, 38, whitePalette)
    # Create label with the text image
    label = Label(menuPage, image=ramenText, bg=redPalette)
    label.place(relx=0.35, rely=0.18, anchor='center')

    # mid red bg
    topBg = ctk.CTkFrame(menuPage, width=475, height=150, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.83, anchor='center')

    myorderText = usingOurFont('MY ORDER:', 280, 38, whitePalette)
    # Create label with the text image
    label = Label(menuPage, image=myorderText, bg=redPalette)
    label.place(relx=0.35, rely=0.78, anchor='center')


    text_photo = usingOurFontWithPadding('CANCEL', 92, 25, whitePalette)
    # cancel button
    cancelButton = ctk.CTkButton(menuPage, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette)
    cancelButton.place(relx=0.2, rely=0.95, anchor='center')

    text_photo = usingOurFontWithPadding('VIEW', 58, 25, whitePalette)
    # view button
    viewButton = ctk.CTkButton(menuPage, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette)
    viewButton.place(relx=0.5, rely=0.95, anchor='center')

    text_photo = usingOurFontWithPadding('PROCEED', 106, 25, whitePalette)
    # proceed button
    proceedButton = ctk.CTkButton(menuPage, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=greenButton)
    proceedButton.place(relx=0.8, rely=0.95, anchor='center')
