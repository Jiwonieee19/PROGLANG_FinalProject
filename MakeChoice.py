from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *
from MenuLists import ramenListImg, donburiListImg, otherListImg

def MakeChoicePage(menuPage, makeChoicePage, item_path): #(unsa e close, unsa e open, unsa e next sa button)

    menuPage.pack_forget()
    makeChoicePage.pack(fill="both", expand=True)
    makeChoicePage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    global makeChoiceTopRightLogo, BgYellow, AddOnBgYellow, DrinksBgYellow, choiceText, label1, label2, label3, selectedItemPhoto

    def goBack():
        makeChoicePage.pack_forget()  # hide current page
        menuPage.pack(fill="both", expand=True)  # show previous page

    # Return button
    makeChoiceReturnPhoto = usingOurFontWithIcon('RETURN', 88, 23, whitePalette, iconPath='reso/FinalReso/ICON/return.png', iconSize=(25, 25))
    makeChoiceReturnButton = ctk.CTkButton(makeChoicePage, width=150, height=50, image=makeChoiceReturnPhoto, text="", corner_radius=10, fg_color=redPalette, command=goBack)
    makeChoiceReturnButton.place(relx=0.2, rely=0.07, anchor='center')

    # Real Logo top right
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    makeChoiceTopRightLogo = ImageTk.PhotoImage(reImg)
    makeChoiceLogoLabel = Label(makeChoicePage, image=makeChoiceTopRightLogo, bg=yellowPalette)
    makeChoiceLogoLabel.place(relx=0.835, rely=0, anchor='n')

    # Top red bg
    makeChoiceTopBg = ctk.CTkFrame(makeChoicePage, width=475, height=740, corner_radius=10, fg_color=redPalette)
    makeChoiceTopBg.place(relx=0.5, rely=0.52, anchor='center')

    choiceText = usingOurFont('MAKE A CHOICE', 280, 38, whitePalette)
    # Create label with the text image
    labelChoice = Label(makeChoicePage, image=choiceText, bg=redPalette)
    labelChoice.place(relx=0.35, rely=0.161, anchor='center')

    # The 3 Frame
    BgYellowImg = Image.open('reso/FinalReso/MakeChoiceBG.png')
    reBgYellowImg = BgYellowImg.resize((267,212))
    BgYellow = ImageTk.PhotoImage(reBgYellowImg)
    BgYellowLabel = Label(makeChoicePage, image=BgYellow, bg=redPalette)
    BgYellowLabel.place(relx=0.33, rely=0.325, anchor='center')

    AddOnBgYellowImg = Image.open('reso/FinalReso/MakeChoiceBG.png')
    reBgYellowImg = AddOnBgYellowImg.resize((455,212))
    AddOnBgYellow = ImageTk.PhotoImage(reBgYellowImg)
    AddOnBgYellowLabel = Label(makeChoicePage, image=AddOnBgYellow, bg=redPalette)
    AddOnBgYellowLabel.place(relx=0.5, rely=0.554, anchor='center')

    DrinksBgYellowImg = Image.open('reso/FinalReso/MakeChoiceBG.png')
    reBgYellowImg = DrinksBgYellowImg.resize((455,212))
    DrinksBgYellow = ImageTk.PhotoImage(reBgYellowImg)
    DrinksBgYellowLabel = Label(makeChoicePage, image=DrinksBgYellow, bg=redPalette)
    DrinksBgYellowLabel.place(relx=0.5, rely=0.783, anchor='center')

    label1 = usingOurFont('ORDER DETAILS', 230, 28, whitePalette)
    # Create label with the text image
    label1Choice = Label(makeChoicePage, image=label1, bg="#852C02")
    label1Choice.place(relx=0.34, rely=0.24, anchor='center')

    label2 = usingOurFont('ADD ONS:', 280, 28, whitePalette)
    # Create label with the text image
    label2Choice = Label(makeChoicePage, image=label2, bg="#852C02")
    label2Choice.place(relx=0.39, rely=0.469, anchor='center')

    label3 = usingOurFont('DRINKS:', 280, 28, whitePalette)
    # Create label with the text image
    label3Choice = Label(makeChoicePage, image=label3, bg="#852C02")
    label3Choice.place(relx=0.39, rely=0.7, anchor='center')

    # Display the clicked item image
    try:
        itemImg = Image.open(item_path)
        # Adjust width and height here (currently 200x240)
        itemImg = itemImg.resize((int(275 / 1.58), int(332 / 1.58)), Image.LANCZOS)
        selectedItemPhoto = ImageTk.PhotoImage(itemImg)
        selectedItemLabel = Label(makeChoicePage, image=selectedItemPhoto, bg=redPalette)
        selectedItemLabel.place(relx=0.76, rely=0.325, anchor='center')
    except Exception as e:
        print(f"Error loading item image: {e}")

    # Cancel button
    makeChoiceCancelPhoto = usingOurFontWithIcon('CANCEL', 92, 23, whitePalette, iconPath='reso/FinalReso/ICON/cancel.png', iconSize=(25, 25))
    makeChoiceCancelButton = ctk.CTkButton(makeChoicePage, width=225, height=50, image=makeChoiceCancelPhoto, text="", corner_radius=10, fg_color=redPalette)
    makeChoiceCancelButton.place(relx=0.27, rely=0.95, anchor='center')

    # Add button
    makeChoiceAddPhoto = usingOurFontWithIcon('ADD ORDER', 120, 23, whitePalette, iconPath='reso/FinalReso/ICON/addtoorder.png', iconSize=(25, 25))
    makeChoiceAddButton = ctk.CTkButton(makeChoicePage, width=225, height=50, image=makeChoiceAddPhoto, text="", corner_radius=10, fg_color=greenButton)
    makeChoiceAddButton.place(relx=0.732, rely=0.95, anchor='center')