import tkinter.ttk as ttk

def configure_scrollbar_style(redPalette, whitePalette):
    """Configure ttk scrollbar style with red palette."""
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except Exception:
        pass
    style.configure(
        "Red.Horizontal.TScrollbar",
        troughcolor=redPalette,
        background=redPalette,
        darkcolor=redPalette,
        lightcolor=redPalette,
        bordercolor=redPalette,
        arrowcolor=whitePalette,
    )
    style.map(
        "Red.Horizontal.TScrollbar",
        background=[("active", redPalette)],
        arrowcolor=[("active", whitePalette)],
    )
    return style
