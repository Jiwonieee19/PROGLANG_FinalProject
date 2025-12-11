from tkinter import *
import tkinter.ttk as ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from DynamicFont import *
from OrderType import *
from CartRender import render_cart
from ScrollbarStyle import configure_scrollbar_style
from MenuLists import ramenListImg, donburiListImg, otherListImg

# Global cart storage
cart_items = []
cart_image_refs = []

def MenuPage(orderTypePage, menuPage):
    orderTypePage.pack_forget()
    menuPage.pack(fill="both", expand=True)
    menuPage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    # Configure scrollbar style
    configure_scrollbar_style(redPalette, whitePalette)

    global topRightLogo, ramenText, myorderText, RAMENPhoto, DONPhoto
    global cart_items, cart_image_refs

    def add_to_cart(img_path, cart_frame):
        cart_items.append(img_path)
        render_cart(cart_frame, cart_items, cart_image_refs, redPalette)

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
    topBg = ctk.CTkFrame(menuPage, width=475, height=560, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.425, anchor='center')

    # mid red bg
    topBg = ctk.CTkFrame(menuPage, width=475, height=180, corner_radius=10, fg_color=redPalette)
    topBg.place(relx=0.5, rely=0.82, anchor='center')

    # frame 1
    frameBg = ctk.CTkFrame(menuPage, width=330, height=570, fg_color=redPalette, bg_color=redPalette)
    frameBg.place(relx=0.63, rely=0.449, anchor='center')

    # Create a frame inside frameBg (non-scrollable)
    image_frame = ctk.CTkFrame(frameBg, fg_color=redPalette)
    image_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Cart strip with bounded height and horizontal scroll
    frame2Bg = ctk.CTkFrame(menuPage, width=465, height=90, corner_radius=10, fg_color=redPalette)
    frame2Bg.place(relx=0.5, rely=0.850, anchor='center')
    frame2Bg.pack_propagate(False)

    cart_canvas = Canvas(frame2Bg, bg=redPalette, highlightthickness=0, height=70, bd=0)
    h_scroll = ttk.Scrollbar(frame2Bg, orient='horizontal', command=cart_canvas.xview, style="Red.Horizontal.TScrollbar")
    cart_canvas.configure(xscrollcommand=h_scroll.set)
    cart_canvas.pack(fill="both", expand=True, side="top")
    h_scroll.pack(fill="x", side="bottom")

    cart_frame = ctk.CTkFrame(cart_canvas, fg_color=redPalette)
    cart_canvas.create_window((0, 0), window=cart_frame, anchor="nw")

    def _sync_scrollregion(event=None):
        cart_canvas.configure(scrollregion=cart_canvas.bbox("all"))

    cart_frame.bind("<Configure>", _sync_scrollregion)

    # Initial render of empty cart
    render_cart(cart_frame, cart_items, cart_image_refs, redPalette)

    # Store references to prevent garbage collection
    image_references = []

    def display_items(item_list, section_name):
        """Clear and display items from the selected section."""
        nonlocal image_references
        
        # Clear previous items
        for widget in image_frame.winfo_children():
            widget.destroy()
        image_references.clear()

        # Display images in 2 columns
        for i, img_path in enumerate(item_list):
            # Create row frame every 2 images
            if i % 2 == 0:
                row_frame = ctk.CTkFrame(image_frame, fg_color=redPalette)
                row_frame.pack(fill="x", padx=5, pady=5)

            try:
                # Load and resize image
                img = Image.open(img_path)
                img = img.resize((110, 132), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                image_references.append(photo)  # Keep reference

                # Create image button without text
                img_button = ctk.CTkButton(row_frame, image=photo, text="", fg_color=redPalette, bg_color=redPalette,
                                           command=lambda p=img_path: add_to_cart(p, cart_frame))
                img_button.pack(side="left", padx=5, pady=5)
            except FileNotFoundError:
                pass  # Skip missing images

    # Display ramen items initially
    display_items(ramenListImg, "RAMEN SECTION")

    ramenText = usingOurFont('RAMEN SECTION', 280, 38, whitePalette)
    # Create label with the text image
    labelRamen = Label(menuPage, image=ramenText, bg=redPalette)
    labelRamen.place(relx=0.35, rely=0.165, anchor='center')

    myorderText = usingOurFont('MY ORDER:', 280, 38, whitePalette)
    # Create label with the text image
    labelMyOrder = Label(menuPage, image=myorderText, bg=redPalette)
    labelMyOrder.place(relx=0.35, rely=0.76, anchor='center')




    RAMENImg = Image.open("reso/FinalReso/RAMEN/RAMEN.png")
    RAMENImg = RAMENImg.resize((110, 110), Image.LANCZOS)
    RAMENPhoto = ImageTk.PhotoImage(RAMENImg)
    # sidebar button
    sideButton1 = ctk.CTkButton(menuPage, image=RAMENPhoto, text="", fg_color=redPalette,  bg_color=redPalette,
                                command=lambda: display_items(ramenListImg, "RAMEN SECTION"))
    sideButton1.place(relx=0.19, rely=0.27, anchor='center')

    DONImg = Image.open("reso/FinalReso/DONBURI/DONBURI.png")
    DONImg = DONImg.resize((110, 110), Image.LANCZOS)
    DONPhoto = ImageTk.PhotoImage(DONImg)
    # sidebar button
    sideButton2 = ctk.CTkButton(menuPage, image=DONPhoto, text="", fg_color=redPalette,  bg_color=redPalette,
                                command=lambda: display_items(donburiListImg, "DONBURI SECTION"))
    sideButton2.place(relx=0.19, rely=0.40, anchor='center')

    OTHERImg = Image.open("reso/FinalReso/OTHERS/OTHERS.png")
    OTHERImg = OTHERImg.resize((110, 110), Image.LANCZOS)
    OTHERPhoto = ImageTk.PhotoImage(OTHERImg)
    # sidebar button
    sideButton3 = ctk.CTkButton(menuPage, image=OTHERPhoto, text="", fg_color=redPalette,  bg_color=redPalette,
                                command=lambda: display_items(otherListImg, "OTHERS SECTION"))
    sideButton3.place(relx=0.19, rely=0.53, anchor='center')


    def Clear(cart_frame):
        global cart_items
        cart_items = []
        render_cart(cart_frame, cart_items, cart_image_refs, redPalette)

   # mid yellow breaker
    topBreaker = ctk.CTkFrame(menuPage, width=5, height=480, corner_radius=3, fg_color=yellowPalette)
    topBreaker.place(relx=0.32, rely=0.453, anchor='center')

    cancelPhoto = usingOurFontWithIcon('CANCEL', 92, 23, whitePalette, iconPath='reso/FinalReso/ICON/cancel.png', iconSize=(25, 25))
    # cancel button
    cancelButton = ctk.CTkButton(menuPage, width=150, height=50, image=cancelPhoto, text="", corner_radius=10, fg_color=redPalette, command=lambda: Clear(cart_frame))
    cancelButton.place(relx=0.2, rely=0.95, anchor='center')

    viewPhoto = usingOurFontWithIcon('VIEW', 58, 23, whitePalette, iconPath='reso/FinalReso/ICON/view.png', iconSize=(25, 25))
    # view button
    viewButton = ctk.CTkButton(menuPage, width=150, height=50, image=viewPhoto, text="", corner_radius=10, fg_color=redPalette)
    viewButton.place(relx=0.485, rely=0.95, anchor='center')

    proceedPhoto = usingOurFontWithIcon('PROCEED', 106, 23, whitePalette, iconPath='reso/FinalReso/ICON/proceed.png', iconSize=(25, 25))
    # proceed button
    proceedButton = ctk.CTkButton(menuPage, width=150, height=50, image=proceedPhoto, text="", corner_radius=10, fg_color=greenButton)
    proceedButton.place(relx=0.785, rely=0.95, anchor='center')

