from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *
from MenuLists import ramenListImg, donburiListImg, otherListImg, item_prices as menu_prices
from MakeChoiceLists import addOnListImg, drinksListImg, item_prices as makechoice_prices

def MakeChoicePage(menuPage, makeChoicePage, item_path): #(unsa e close, unsa e open, unsa e next sa button)

    menuPage.pack_forget()
    makeChoicePage.pack(fill="both", expand=True)
    makeChoicePage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    global makeChoiceTopRightLogo, BgYellow, AddOnBgYellow, DrinksBgYellow, choiceText, label1, label2, label3, selectedItemPhoto
    global addOnImageRefs, drinksImageRefs, orderDetailsLabel
    global addOnPhotosNormal, addOnPhotosSelected, addOnButtons
    global drinkPhotosNormal, drinkPhotosSelected, drinkButtons

    addOnImageRefs = []
    drinksImageRefs = []
    addOnPhotosNormal, addOnPhotosSelected, addOnButtons = [], [], []
    drinkPhotosNormal, drinkPhotosSelected, drinkButtons = [], [], []

    def _hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def _darken_photo(img, overlay_hex="#730C03", alpha=120):
        rgb = _hex_to_rgb(overlay_hex)
        overlay = Image.new('RGBA', img.size, (*rgb, alpha))
        base = img.convert('RGBA')
        return Image.alpha_composite(base, overlay)
    
    def calculate_total_cost():
        """Calculate total cost from dish, add-ons, and drinks."""
        total = 0
        # Get dish price
        total += menu_prices.get(order["item"], 0)
        # Get add-ons price
        for addon in order["addOns"]:
            total += makechoice_prices.get(addon, 0)
        # Get drinks price
        for drink in order["drinks"]:
            total += makechoice_prices.get(drink, 0)
        return total
    
    # Order tracking
    order = {"item": "", "addOns": [], "drinks": []}
    
    # Extract item name from path
    item_name = item_path.split("/")[-1].replace(".png", "")
    order["item"] = item_name
    selected_drink_index = None
    
    def update_order_details():
        """Update the order details and cost display (no dish line)."""
        addons_text = ', '.join(order['addOns']) if order['addOns'] else "NONE"
        drinks_text = ', '.join(order['drinks']) if order['drinks'] else "NONE"
        total = calculate_total_cost()
        
        details_text = f"ADD ONS:  {addons_text}\nDRINKS:  {drinks_text}\nTOTAL COST:  {total}.00 PHP"
        
        # Update label if it exists
        try:
            orderDetailsLabel.config(text=details_text)
        except:
            pass
    
    def toggle_addon(addon_name, addon_index):
        """Toggle add-on selection."""
        if addon_name in order["addOns"]:
            order["addOns"].remove(addon_name)
            try:
                addOnButtons[addon_index].configure(image=addOnPhotosNormal[addon_index])
            except Exception:
                pass
        else:
            order["addOns"].append(addon_name)
            try:
                addOnButtons[addon_index].configure(image=addOnPhotosSelected[addon_index])
            except Exception:
                pass
        update_order_details()
    
    def toggle_drink(drink_name, drink_index):
        """Toggle drink selection."""
        nonlocal selected_drink_index
        # If clicking the currently selected drink, deselect it
        if selected_drink_index == drink_index and drink_name in order["drinks"]:
            order["drinks"].clear()
            drinkButtons[drink_index].configure(image=drinkPhotosNormal[drink_index])
            selected_drink_index = None
            update_order_details()
            return

        # Deselect previously selected drink if any
        if selected_drink_index is not None:
            prev_idx = selected_drink_index
            # Reset image and clear order drinks
            drinkButtons[prev_idx].configure(image=drinkPhotosNormal[prev_idx])
            order["drinks"].clear()

        # Select the new drink
        order["drinks"].append(drink_name)
        drinkButtons[drink_index].configure(image=drinkPhotosSelected[drink_index])
        selected_drink_index = drink_index
        update_order_details()

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

    # Display add-ons horizontally
    addOnStartX = 0.235
    addOnSpacing = 0.26
    # Use names that match MakeChoiceLists.item_prices keys
    addOnNames = ["EGG", "NOODLE", "SEAWEEDS"]
    addOnNameToPath = {name: path for name, path in zip(addOnNames, addOnListImg)}
    for i, img_path in enumerate(addOnListImg):
        try:
            # Load and resize image
            img = Image.open(img_path)
            img = img.resize((int(219/1.8), int(264/1.8)), Image.LANCZOS)
            photo_normal = ImageTk.PhotoImage(img)
            dark_img = _darken_photo(img, redPalette, 120)
            photo_selected = ImageTk.PhotoImage(dark_img)
            addOnPhotosNormal.append(photo_normal)
            addOnPhotosSelected.append(photo_selected)
            
            # Create image button with toggle function
            addon_name = addOnNames[i]
            img_button = ctk.CTkButton(makeChoicePage, image=photo_normal, text="", 
                                       fg_color="#CDAE00", bg_color="#CDAE00",
                                       width=80, height=96, corner_radius=10,
                                       command=lambda idx=i, name=addon_name: toggle_addon(name, idx))
            img_button.place(relx=addOnStartX + (i * addOnSpacing), rely=0.580, anchor='center')
            addOnButtons.append(img_button)
        except FileNotFoundError:
            pass

    DrinksBgYellowImg = Image.open('reso/FinalReso/MakeChoiceBG.png')
    reBgYellowImg = DrinksBgYellowImg.resize((455,212))
    DrinksBgYellow = ImageTk.PhotoImage(reBgYellowImg)
    DrinksBgYellowLabel = Label(makeChoicePage, image=DrinksBgYellow, bg=redPalette)
    DrinksBgYellowLabel.place(relx=0.5, rely=0.783, anchor='center')

    # Display drinks horizontally
    drinkStartX = 0.235
    drinkSpacing = 0.26
    # Use names that match MakeChoiceLists.item_prices keys
    drinkNames = ["COCA COLA", "FANTA", "PEPSI"]
    drinkNameToPath = {name: path for name, path in zip(drinkNames, drinksListImg)}
    for i, img_path in enumerate(drinksListImg):
        try:
            # Load and resize image
            img = Image.open(img_path)
            img = img.resize((int(219/1.8), int(264/1.8)), Image.LANCZOS)
            photo_normal = ImageTk.PhotoImage(img)
            dark_img = _darken_photo(img, redPalette, 120)
            photo_selected = ImageTk.PhotoImage(dark_img)
            drinkPhotosNormal.append(photo_normal)
            drinkPhotosSelected.append(photo_selected)
            
            # Create image button with toggle function
            drink_name = drinkNames[i]
            img_button = ctk.CTkButton(makeChoicePage, image=photo_normal, text="", 
                                       fg_color="#CDAE00", bg_color="#CDAE00",
                                       width=80, height=96, corner_radius=10,
                                       command=lambda idx=i, name=drink_name: toggle_drink(name, idx))
            img_button.place(relx=drinkStartX + (i * drinkSpacing), rely=0.809, anchor='center')
            drinkButtons.append(img_button)
        except FileNotFoundError:
            pass

    # Order details display on first yellow background
    orderDetailsLabel = Label(makeChoicePage, text="", 
                              font=("Baloo Tammudu", 11), bg="#CDAE00", fg=redPalette, 
                              justify="left")
    orderDetailsLabel.place(relx=0.1, rely=0.353, anchor='w')
    
    # Initialize with full details including 'none' for empty items
    update_order_details()

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
    # cancel acts like return
    makeChoiceCancelButton = ctk.CTkButton(makeChoicePage, width=225, height=50, image=makeChoiceCancelPhoto, text="", corner_radius=10, fg_color=redPalette, command=goBack)
    makeChoiceCancelButton.place(relx=0.27, rely=0.95, anchor='center')

    # Add button
    makeChoiceAddPhoto = usingOurFontWithIcon('ADD ORDER', 120, 23, whitePalette, iconPath='reso/FinalReso/ICON/addtoorder.png', iconSize=(25, 25))
    # add order: confirm selections, add to cart, and return to menu
    def _confirm_and_add_to_cart():
        """Send selected dish/add-ons/drink to cart and return to menu."""
        try:
            from Menu import append_cart_item

            # Resolve add-on image paths for selected names
            selected_addon_paths = []
            for name in order["addOns"]:
                path = addOnNameToPath.get(name)
                if path:
                    selected_addon_paths.append(path)

            # Resolve drink image path (single selection list)
            selected_drink_paths = []
            for name in order["drinks"]:
                path = drinkNameToPath.get(name)
                if path:
                    selected_drink_paths.append(path)

            order_entry = {
                "dish": item_path,
                "addOns": selected_addon_paths,
                "drinks": selected_drink_paths,
            }

            append_cart_item(order_entry)
        except Exception as e:
            print(f"Failed to append cart item: {e}")
        # Navigate back to menu
        goBack()

    makeChoiceAddButton = ctk.CTkButton(makeChoicePage, width=225, height=50, image=makeChoiceAddPhoto, text="", corner_radius=10, fg_color=greenButton, command=_confirm_and_add_to_cart)
    makeChoiceAddButton.place(relx=0.732, rely=0.95, anchor='center')