from tkinter import *
from PIL import Image, ImageTk
from Menu import MenuPage

def OrderTypePage(landingPage, orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage): #(unsa e close, unsa e open, unsa e next sa button)

    landingPage.pack_forget()
    orderTypePage.pack(fill="both", expand=True)
    orderTypePage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"

    global landingLogo, DineIn, TakeOut, English, Tagalog, Bisaya
    # Real Logo center
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    landingLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(orderTypePage, image=landingLogo, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0.15, anchor='center')

    label = Label(orderTypePage, text="ORDER TYPE", font=('Baloo Tammudu', 26), fg=whitePalette, bg=yellowPalette)
    label.place(relx=0.5, rely=0.34, anchor='center')

    label = Label(orderTypePage, text="SELECT YOUR LANGUAGE", font=('Baloo Tammudu', 26), fg=whitePalette, bg=yellowPalette)
    label.place(relx=0.5, rely=0.75, anchor='center')

    # 2 button 1 Frame
    DineInImg = Image.open('reso/dineIn.png')
    reDineInImg = DineInImg.resize((163,222))
    DineIn = ImageTk.PhotoImage(reDineInImg)

    TakeOutImg = Image.open('reso/takeOut.png')
    reTakeOutImg = TakeOutImg.resize((163,222))
    TakeOut = ImageTk.PhotoImage(reTakeOutImg)

    # Create a frame inside landingWindow
    buttonFrame = Frame(orderTypePage, bg=yellowPalette)
    buttonFrame.place(relx=0.5, rely=0.5, anchor='center')

    # First button
    startButton = Button(buttonFrame, image=DineIn, bg=yellowPalette, borderwidth=0, highlightthickness=0, command=lambda: MenuPage(orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage))
    startButton.pack(side=LEFT, padx=20)   # spacing between buttons

    # Second button
    optionButton = Button(buttonFrame, image=TakeOut, bg=yellowPalette, borderwidth=0, highlightthickness=0, command=lambda: MenuPage(orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage))
    optionButton.pack(side=LEFT, padx=20)


    # # 3 button 1 Frame
    EnglishImg = Image.open('reso/english.png')
    reEnglishImg = EnglishImg.resize((132,70))
    English = ImageTk.PhotoImage(reEnglishImg)

    TagalogImg = Image.open('reso/tagalog.png')
    reTagalogImg = TagalogImg.resize((132,70))
    Tagalog = ImageTk.PhotoImage(reTagalogImg)

    BisayaImg = Image.open('reso/bisaya1.png')
    reBisayaImg = BisayaImg.resize((132,70))
    Bisaya = ImageTk.PhotoImage(reBisayaImg)

    # Create a frame inside orderTypePage
    buttonFrame1 = Frame(orderTypePage, bg=yellowPalette)
    buttonFrame1.place(relx=0.5, rely=0.83, anchor='center')

    # First button
    startButton = Button(buttonFrame1, image=English, bg=yellowPalette, borderwidth=0, highlightthickness=0)
    startButton.pack(side=LEFT, padx=10)

    # Second button
    optionButton = Button(buttonFrame1, image=Tagalog, bg=yellowPalette, borderwidth=0, highlightthickness=0)
    optionButton.pack(side=LEFT, padx=10)

    # Third button
    optionButton = Button(buttonFrame1, image=Bisaya, bg=yellowPalette, borderwidth=0, highlightthickness=0)
    optionButton.pack(side=LEFT, padx=10)