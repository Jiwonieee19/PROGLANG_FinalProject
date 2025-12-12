# import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Intro import IntroPage
from OrderType import OrderTypePage

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
# menuRamenPage = Frame(root)
# menuDonburiPage = Frame(root)
# menuOthersPage = Frame(root)

yellowPalette = "#CDAE00"
redPalette = "#730C03"
whitePalette = "#FFFFFF"

# Manipulating the headbar doesnt matter since we will remove this to achieve kiosk
root.title("Python - KIOSK")
iconLogo = PhotoImage(file='reso/LOGO.png')
root.iconphoto(True, iconLogo)
root.resizable(False, False)

landingPage.pack(fill="both", expand=True)
landingPage.config(background=yellowPalette)

# IntroPage(root, landingPage)

# Ads/Promo
ads = ['reso/3rdAd.png', 'reso/1stAd.png', 'reso/2ndAd.png']

# Preload the images ONCE
preloaded_ads = []
for a in ads:
    img = Image.open(a).resize((486, 738))
    preloaded_ads.append(ImageTk.PhotoImage(img))

ad_index = 0

adLabel = Label(landingPage, bg=yellowPalette)
adLabel.place(relx=0.06, rely=0.02, anchor='nw')

def rotate_ad():
    global ad_index
    adLabel.config(image=preloaded_ads[ad_index])
    ad_index = (ad_index + 1) % len(preloaded_ads)
    landingPage.after(2100, rotate_ad)

rotate_ad()


# Real Logo top left
img = Image.open('reso/realLogo.png')
reImg = img.resize((120,108))
landingLogo = ImageTk.PhotoImage(reImg)
logoLabel = Label(landingPage, image=landingLogo, bg=yellowPalette)
logoLabel.place(relx=0.02, rely=0, anchor='nw')

btnStart = Button(landingPage, text="TAP TO START", font=('Baloo Tammudu', 30), fg=whitePalette, bg=redPalette, borderwidth=0, highlightthickness=0, command=lambda: OrderTypePage(landingPage, orderTypePage, menuPage, makeChoicePage, reviewOrderPage, lastPage))
# btnStart = ctk.CTkButton(landingPage, text="TAP TO START", font=('Baloo Tammudu', 30),  width=492, height=141, fg_color=whitePalette, bg_color=redPalette, command=lambda: OrderTypePage(landingPage, orderTypePage, orderRamenPage))
btnStart.place(relx=0.5, rely=0.895, width=500, height=141, anchor='center')

root.mainloop()
