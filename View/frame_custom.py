import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


class FrameCustom(tk.Frame):
    def __init__(self, parent):
        self.bgc_color = "#5F5980"
        self.light_bgc_color = "#756F9B"
        self.clicked_bgc_color = "#807BA3"
        self.text_color = "#FFFFFF"

        self.helvetica_12 = Font(family="Helvetica", size="12")
        self.helvetica_16 = Font(family="Helvetica", size="16")
        self.helvetica_24 = Font(family="Helvetica", size="24")

        tk.Frame.__init__(self, parent, bg=self.bgc_color)