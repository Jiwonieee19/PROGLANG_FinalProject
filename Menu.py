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

    global topRightLogo, ramenText, myorderText, RAMENPhoto, DONPhoto

    def goBack():
        menuPage.pack_forget()      # hide current page
        orderTypePage.pack(fill="both", expand=True)  # show previous page

    # sections = ['Ramen', 'Donburi', 'Others']

    # btnRamen = Button(menuPage, text="RAMEN", font=('Baloo Tammudu', 45))
    # btnDonburi = Button(menuPage, text="DONBURI", font=('Baloo Tammudu', 45))
    # btnOthers = Button(menuPage, text="OTHERS", font=('Baloo Tammudu', 45))

    text_photo = usingOurFontWithIcon('RETURN', 88, 23, whitePalette, iconPath='reso/FinalReso/ICON/return.png', iconSize=(25, 25))
    # return button
    returnButton = ctk.CTkButton(menuPage, width=150, height=50, image=text_photo, text="", corner_radius=10, fg_color=redPalette, command=goBack)
    returnButton.place(relx=0.2, rely=0.07, anchor='center')

    # Real Logo top right
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    topRightLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(menuPage, image=topRightLogo, bg=yellowPalette)
    logoLabel.place(relx=0.835, rely=0, anchor='n')


    # top red bg
    topBg = ctk.CTkFrame(menuPage, width=475, height=575, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.435, anchor='center')

    # mid red bg
    topBg = ctk.CTkFrame(menuPage, width=475, height=150, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.83, anchor='center')

    ramenText = usingOurFont('RAMEN SECTION', 280, 38, whitePalette)
    # Create label with the text image
    labelRamen = Label(menuPage, image=ramenText, bg=redPalette)
    labelRamen.place(relx=0.35, rely=0.165, anchor='center')

    myorderText = usingOurFont('MY ORDER:', 280, 38, whitePalette)
    # Create label with the text image
    labelMyOrder = Label(menuPage, image=myorderText, bg=redPalette)
    labelMyOrder.place(relx=0.35, rely=0.78, anchor='center')




    RAMENImg = Image.open("reso/FinalReso/RAMEN/RAMEN.png")
    RAMENImg = RAMENImg.resize((110, 110), Image.LANCZOS)
    RAMENPhoto = ImageTk.PhotoImage(RAMENImg)
    # sidebar button
    sideButton1 = ctk.CTkButton(menuPage, image=RAMENPhoto, text="", fg_color=redPalette,  bg_color=redPalette)
    sideButton1.place(relx=0.19, rely=0.27, anchor='center')

    DONImg = Image.open("reso/FinalReso/DONBURI/DONBURI.png")
    DONImg = DONImg.resize((110, 110), Image.LANCZOS)
    DONPhoto = ImageTk.PhotoImage(DONImg)
    # sidebar button
    sideButton2 = ctk.CTkButton(menuPage, image=DONPhoto, text="", fg_color=redPalette,  bg_color=redPalette)
    sideButton2.place(relx=0.19, rely=0.40, anchor='center')

    OTHERImg = Image.open("reso/FinalReso/OTHERS/OTHERS.png")
    OTHERImg = OTHERImg.resize((110, 110), Image.LANCZOS)
    OTHERPhoto = ImageTk.PhotoImage(OTHERImg)
    # sidebar button
    sideButton3 = ctk.CTkButton(menuPage, image=OTHERPhoto, text="", fg_color=redPalette,  bg_color=redPalette)
    sideButton3.place(relx=0.19, rely=0.53, anchor='center')



   # mid yellow breaker
    topBreaker = ctk.CTkFrame(menuPage, width=5, height=495, corner_radius=3, fg_color=yellowPalette)
    topBreaker.place(relx=0.32, rely=0.455, anchor='center')

    cancelPhoto = usingOurFontWithIcon('CANCEL', 92, 23, whitePalette, iconPath='reso/FinalReso/ICON/cancel.png', iconSize=(25, 25))
    # cancel button
    cancelButton = ctk.CTkButton(menuPage, width=150, height=50, image=cancelPhoto, text="", corner_radius=10, fg_color=redPalette)
    cancelButton.place(relx=0.2, rely=0.95, anchor='center')

    viewPhoto = usingOurFontWithIcon('VIEW', 58, 23, whitePalette, iconPath='reso/FinalReso/ICON/view.png', iconSize=(25, 25))
    # view button
    viewButton = ctk.CTkButton(menuPage, width=150, height=50, image=viewPhoto, text="", corner_radius=10, fg_color=redPalette)
    viewButton.place(relx=0.485, rely=0.95, anchor='center')

    proceedPhoto = usingOurFontWithIcon('PROCEED', 106, 23, whitePalette, iconPath='reso/FinalReso/ICON/proceed.png', iconSize=(25, 25))
    # proceed button
    proceedButton = ctk.CTkButton(menuPage, width=150, height=50, image=proceedPhoto, text="", corner_radius=10, fg_color=greenButton)
    proceedButton.place(relx=0.785, rely=0.95, anchor='center')

