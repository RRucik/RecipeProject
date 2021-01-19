import tkinter as tk

from View import frame_methods
from View.frame_search import FrameSearch
from View.frame_select import FrameSelect
from View.frame_add_edit import FrameAddEdit


class View(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(pady=(0, 0))
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.create_class_frame(FrameSearch, "FrameSearch")
        self.create_class_frame(FrameSelect, "FrameSelect")
        self.create_class_frame(FrameAddEdit, "FrameAdd")
        self.create_class_frame(FrameAddEdit, "FrameEdit")

        self.menu_bar = tk.Menu(self)
        self.menu = tk.Menu(self.menu_bar, tearoff=0)

    def create_class_frame(self, frame_class, frame_name):
        new_frame = frame_class(parent=self.container)
        self.frames[frame_name] = new_frame
        new_frame.grid(row=0, column=0, sticky="nsew")

    def create_app_menu(self):
        self.menu_bar.add_cascade(label="File", menu=self.menu)
        self.config(menu=self.menu_bar)

    def set_app_background(self, bgc_path):
        frame_methods.set_app_background(self, bgc_path)

    @staticmethod
    def set_styles():
        frame_methods.set_style()

    @staticmethod
    def get_selected_name(tree_view):
        return frame_methods.get_selected_from_tree(tree_view)

    @staticmethod
    def get_data_from_entries(entries):
        return frame_methods.get_data_from_entries(entries)

    @staticmethod
    def get_data_from_text_view(text_view):
        return frame_methods.get_data_from_text_view(text_view)

    @staticmethod
    def get_data_from_tree_view(tree_view):
        return frame_methods.get_data_from_tree(tree_view)

    @staticmethod
    def insert_to_recipe_tree(tree_view, recipe_list):
        return frame_methods.insert_to_recipes_tree(tree_view, recipe_list)

    @staticmethod
    def insert_to_ing_tree(tree_view, ing_list):
        return frame_methods.insert_to_ing_tree(tree_view, ing_list)

    @staticmethod
    def clear_tree_view(tree_view):
        frame_methods.clear_tree_view(tree_view)

    def configure_gui(self):
        photo = tk.PhotoImage(file="../pictures/app_icon.png")
        self.title("Recipe saver")
        self.iconphoto(False, photo)
        self.resizable(False, False)
        self.set_styles()
        self.create_app_menu()

    def start_gui(self):
        self.mainloop()
