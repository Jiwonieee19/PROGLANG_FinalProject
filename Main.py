# import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Intro import IntroPage
from OrderType import OrderTypePage
from DynamicFont import usingOurFontWithHeight

root = Tk()

root.geometry("540x960+583+20")

introPage = Frame(root)
landingPage = Frame(root)
orderPage = Frame(root)
orderTypePage = Frame(root)
makeChoicePage = Frame(root)
reviewOrderPage = Frame(root)
lastPage = Frame(root)

menuPage = Frame(root)

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

root.title("Python - KIOSK")
iconLogo = PhotoImage(file='reso/LOGO.png')
root.iconphoto(True, iconLogo)
root.resizable(False, False)

landingPage.pack(fill="both", expand=True)
landingPage.config(background=yellowPalette)

IntroPage(root, landingPage)

ads = ['reso/3rdAd.png', 'reso/1stAd.png', 'reso/2ndAd.png']

preloadedAds = []
for a in ads:
    img = Image.open(a).resize((486, 738))
    preloadedAds.append(ImageTk.PhotoImage(img))

adIndex = 0

adLabel = Label(landingPage, bg=yellowPalette)
adLabel.place(relx=0.06, rely=0.02, anchor='nw')

def rotate_ad():
    global adIndex
    adLabel.config(image=preloadedAds[adIndex])
    adIndex = (adIndex + 1) % len(preloadedAds)
    landingPage.after(2100, rotate_ad)

rotate_ad()


# Real Logo top left
img = Image.open('reso/realLogo.png')
reImg = img.resize((120,108))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingPage, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.02, rely=0, anchor='nw')

# btnStart = Button(landingPage, text="TAP TO START", font=('Baloo Tammudu', 30), fg=whitePalette, bg=redPalette, borderwidth=0, highlightthickness=0, command=lambda: OrderTypePage(landingPage, orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage))
text_photo = usingOurFontWithHeight('TAP TO START', 492, 141, 50, whitePalette, 90, 30)
# Create label with the text image
startButton = Button(landingPage, image=text_photo, bg=redPalette, borderwidth=0, highlightthickness=0, command=lambda: OrderTypePage(landingPage, orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage))
startButton.place(relx=0.5, rely=0.895, anchor='center')

root.mainloop()
