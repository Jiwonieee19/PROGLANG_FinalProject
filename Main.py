
# import tkinter as tk
from tkinter import *

root = Tk()

root.geometry("540x960+583+20")

landingPage = Frame(root)
orderPage = Frame(root)

orderTypePage = Frame(root)
orderRamenPage = Frame(root)
orderDonburiPage = Frame(root)
orderOthersPage = Frame(root)

landingPage.pack(fill="both", expand=True)


def go_to_order_type():
    landingPage.pack_forget()
    orderTypePage.pack(fill="both", expand=True)

    btnDineIn = Button(orderTypePage, text="DINE-IN", font=('Baloo Tammudu', 45), command=go_to_order)
    btnTakeOut = Button(orderTypePage, text="TAKE OUT", font=('Baloo Tammudu', 45), command=go_to_order)

    btnDineIn.pack()
    btnTakeOut.pack()

btnStart = Button(landingPage, text="TAP TO START", font=('Baloo Tammudu', 80), command=go_to_order_type)
btnStart.pack()

def show_ramen_items():
    menu = {
        "Ramen": {
            "Shoyu": 349,
            "Spicy Miso": 369,
            "Tonkotsu": 399
        },
        "Donburi": {
            "Beef": 180,
            "Chicken": 170,
            "Vegetable": 150
        },
        "Others": {
            "Beef": 180,
            "Chicken": 170,
            "Vegetable": 150
        }
    }

def go_to_order():
    orderTypePage.pack_forget()
    orderPage.pack(fill="both", expand=True)

    sections = ['Ramen', 'Donburi', 'Others']

    btnRamen = Button(orderPage, text="RAMEN", font=('Baloo Tammudu', 45), command=show_ramen_items)
    btnDonburi = Button(orderPage, text="DONBURI", font=('Baloo Tammudu', 45))
    btnOthers = Button(orderPage, text="OTHERS", font=('Baloo Tammudu', 45))

    btnRamen.pack()
    btnDonburi.pack()
    btnOthers.pack()

    


root.mainloop()
