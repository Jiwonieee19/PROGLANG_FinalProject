from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from DynamicFont import *
import tkinter.ttk as ttk
from ScrollbarStyle import configure_scrollbar_style

def ReviewOrderPage (menuPage, reviewOrderPage, lastPage): #(unsa e close, unsa e open, unsa e next sa button)
    from Menu import cart_items  # Import cart_items from Menu

    menuPage.pack_forget()
    reviewOrderPage.pack(fill="both", expand=True)
    reviewOrderPage.config(background="#CDAE00")

    yellowPalette = "#CDAE00"
    redPalette = "#730C03"
    whitePalette = "#FFFFFF"
    greenButton = "#167303"

    # Configure scrollbar style
    configure_scrollbar_style(redPalette, whitePalette)

    global reviewTopRightLogo, ReviewBg, reviewText, order_image_refs

    # Keep image references
    order_image_refs = []

    def goBack():
        reviewOrderPage.pack_forget()
        menuPage.pack(fill="both", expand=True)

    def checkout():
        try:
            # clear cart and refresh strip
            from Menu import cart_items as _ci, menu_cart_frame as _cart_frame, menu_red_palette as _red, cart_image_refs as _imgrefs
            from CartRender import render_cart
            _ci.clear()
            if _cart_frame is not None and _red is not None:
                render_cart(_cart_frame, _ci, _imgrefs, _red)
        except Exception:
            pass
        # navigate to last page via LastPage(reviewOrderPage, lastPage)
        try:
            from lastPage import LastPage
            LastPage(reviewOrderPage, lastPage)
        except Exception:
            # fallback to simple pack if import fails
            reviewOrderPage.pack_forget()
            lastPage.pack(fill="both", expand=True)

    # Real Logo top right
    img = Image.open('reso/realLogo.png')
    reImg = img.resize((120,108))
    reviewTopRightLogo = ImageTk.PhotoImage(reImg)
    logoLabel = Label(reviewOrderPage, image=reviewTopRightLogo, bg=yellowPalette)
    logoLabel.place(relx=0.5, rely=0, anchor='n')

    # top red bg
    ReviewBg = ctk.CTkFrame(reviewOrderPage, width=475, height=750, corner_radius=10, fg_color=redPalette)
    ReviewBg.place(relx=0.5, rely=0.52, anchor='center')

    reviewText = usingOurFont('REVIEW YOUR ORDER', 370, 38, whitePalette)
    # Create label with the text image
    labelChoice = Label(reviewOrderPage, image=reviewText, bg=redPalette)
    labelChoice.place(relx=0.5, rely=0.161, anchor='center')

    # Create scrollable frame for orders
    canvas = Canvas(ReviewBg, bg=redPalette, highlightthickness=0, width=455, height=620)
    canvas.place(relx=0.5, rely=0.57, anchor='center')

    scrollbar = ttk.Scrollbar(ReviewBg, orient="vertical", command=canvas.yview, style="Custom.Vertical.TScrollbar")
    scrollbar.place(relx=0.96, rely=0.57, anchor='center', height=620)

    scrollable_frame = Frame(canvas, bg=redPalette)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Display each order with header if cart has items
    if cart_items:
        # helper to delete specific order and refresh
        def delete_order(index_zero_based):
            try:
                # remove from cart and refresh both cart strip and review page
                from Menu import cart_items as _ci, menu_cart_frame as _cart_frame, menu_red_palette as _red, cart_image_refs as _imgrefs
                from CartRender import render_cart
                if 0 <= index_zero_based < len(_ci):
                    del _ci[index_zero_based]
                    # refresh cart strip if available
                    if _cart_frame is not None and _red is not None:
                        render_cart(_cart_frame, _ci, _imgrefs, _red)
                    # refresh review page
                    reviewOrderPage.pack_forget()
                    ReviewOrderPage(menuPage, reviewOrderPage, lastPage)
            except Exception:
                pass

        for idx, order in enumerate(cart_items, start=1):
            # Normalize legacy strings into dict entries
            if isinstance(order, str):
                order = {"dish": order, "addOns": [], "drinks": []}

            # Order header row (label + delete button aligned to order frame edge)
            headerRow = Frame(scrollable_frame, bg=redPalette)
            headerRow.pack(fill='x', anchor='w', pady=(3, 5), padx=0)

            orderHeaderText = usingOurFont(f'ORDER {idx}', 200, 28, whitePalette)
            headerLabel = Label(headerRow, image=orderHeaderText, bg=redPalette)
            headerLabel.image = orderHeaderText  # Keep reference
            headerLabel.pack(side=LEFT)

            # delete icon button on the right edge
            try:
                delImg = Image.open('reso/FinalReso/ICON/delete.png')
                delImg = delImg.resize((28, 28), Image.LANCZOS)
                delPhoto = ImageTk.PhotoImage(delImg)
                order_image_refs.append(delPhoto)
                delBtn = ctk.CTkButton(headerRow, width=32, height=32, image=delPhoto, text="", corner_radius=6, fg_color=redPalette, hover_color="#8B1A10", command=lambda i=idx-1: delete_order(i))
                delBtn.pack(side=RIGHT, padx=(0, 8))
            except Exception:
                pass

            # Count total items to calculate height
            total_items = 0
            if order.get("dish"):
                total_items += 1
            if order.get("addOns"):
                total_items += len(order["addOns"])
            if order.get("drinks"):
                total_items += len(order["drinks"])
            
            # Calculate rows needed (3 items per row)
            rows_needed = (total_items + 2) // 3  # ceiling division
            frame_height = max(212, rows_needed * 162)  # 162 = image height (132) + padding (30)

            # Order frame background
            orderFrame = ctk.CTkFrame(scrollable_frame, width=435, height=frame_height, corner_radius=10, fg_color=yellowPalette)
            orderFrame.pack(pady=(0, 15))
            orderFrame.pack_propagate(False)

            # Create inner frame for all images with wrapping
            contentFrame = Frame(orderFrame, bg=yellowPalette)
            contentFrame.pack(anchor='nw', padx=10, pady=10)

            # Collect all images to display
            all_images = []
            
            # Dish image
            if order.get("dish"):
                try:
                    dishImg = Image.open(order["dish"])
                    dishImg = dishImg.resize((110, 132), Image.LANCZOS)
                    dishPhoto = ImageTk.PhotoImage(dishImg)
                    order_image_refs.append(dishPhoto)
                    all_images.append(dishPhoto)
                except:
                    pass

            # Add-ons images (same size as dish)
            if order.get("addOns") and len(order["addOns"]) > 0:
                for addOn in order["addOns"]:
                    try:
                        addOnImg = Image.open(addOn)
                        addOnImg = addOnImg.resize((110, 132), Image.LANCZOS)
                        addOnPhoto = ImageTk.PhotoImage(addOnImg)
                        order_image_refs.append(addOnPhoto)
                        all_images.append(addOnPhoto)
                    except:
                        pass

            # Drinks images (same size as dish)
            if order.get("drinks") and len(order["drinks"]) > 0:
                for drink in order["drinks"]:
                    try:
                        drinkImg = Image.open(drink)
                        drinkImg = drinkImg.resize((110, 132), Image.LANCZOS)
                        drinkPhoto = ImageTk.PhotoImage(drinkImg)
                        order_image_refs.append(drinkPhoto)
                        all_images.append(drinkPhoto)
                    except:
                        pass

            # Display images in rows of 3
            current_row = Frame(contentFrame, bg=yellowPalette)
            current_row.pack(anchor='w')
            
            for i, photo in enumerate(all_images):
                if i > 0 and i % 3 == 0:
                    # Create new row after every 3 images
                    current_row = Frame(contentFrame, bg=yellowPalette)
                    current_row.pack(anchor='w')
                
                # Frame with red background and border radius for each image
                imgFrame = ctk.CTkFrame(current_row, fg_color=redPalette, corner_radius=5, width=120, height=142)
                imgFrame.pack(side=LEFT, padx=5, pady=5)
                imgFrame.pack_propagate(False)
                
                imgLabel = Label(imgFrame, image=photo, bg=redPalette)
                imgLabel.pack(expand=True)


    backPhoto = usingOurFontWithIcon('BACK', 58, 23, whitePalette, iconPath='reso/FinalReso/ICON/return.png', iconSize=(25, 25))
    # back button
    backButton = ctk.CTkButton(reviewOrderPage, width=225, height=50, image=backPhoto, text="", corner_radius=10, fg_color=redPalette, command=lambda: goBack())
    backButton.place(relx=0.27, rely=0.95, anchor='center')

    checkoutPhoto = usingOurFontWithIcon('CHECKOUT', 114, 23, whitePalette, iconPath='reso/FinalReso/ICON/checkout.png', iconSize=(25, 25))
    # checkout button (disabled and black if cart is empty)
    if cart_items and len(cart_items) > 0:
        checkoutButton = ctk.CTkButton(reviewOrderPage, width=225, height=50, image=checkoutPhoto, text="", corner_radius=10, fg_color=greenButton, command=checkout)
    else:
        checkoutButton = ctk.CTkButton(reviewOrderPage, width=225, height=50, image=checkoutPhoto, text="", corner_radius=10, fg_color="#000000")
        try:
            checkoutButton.configure(state="disabled")
        except Exception:
            pass
    checkoutButton.place(relx=0.732, rely=0.95, anchor='center')