from tkinter import *
from PIL import Image, ImageTk

def IntroPage(root, landingPage):
    
    landingPage.pack_forget()
    introPage = Frame(root, width=540, height=960, bg="#CDAE00")
    introPage.pack(fill="both", expand=True)

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"

    global landingLogo

    img = Image.open('reso/landingLogo.png')
    reImg = img.resize((221,229))
    landingLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(introPage, image=landingLogo, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0.3, anchor='center')

    label = Label(introPage, text='"Where Noodles hug the Soul."', font=('Baloo Tammudu', 18), fg=whitePalette, bg=yellowPalette)
    label.place(relx=0.5, rely=0.59, anchor='center')

    def showLanding():
        introPage.destroy()
        landingPage.pack(fill="both", expand=True)

    root.after(3500, showLanding) 