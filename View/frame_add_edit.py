import tkinter as tk
from tkinter import filedialog

from View import frame_custom
from View import frame_methods
from PIL import Image, ImageTk


class FrameAddEdit(frame_custom.FrameCustom):
    def __init__(self, parent):
        frame_custom.FrameCustom.__init__(self, parent)

        # Frame setup
        self.frame_toolbar = tk.Frame(self, bg=self.bgc_color)
        self.frame_top = tk.Frame(self, bg=self.bgc_color)
        self.frame_bot = tk.Frame(self, bg=self.bgc_color)
        self.frame_toolbar.pack(side=tk.TOP, padx=10, pady=(5, 0), fill=tk.BOTH)
        self.frame_top.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        self.frame_bot.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH)

        self.frame_top_one = tk.Frame(self.frame_top, bg=self.bgc_color)
        self.frame_top_two = tk.Frame(self.frame_top, bg=self.bgc_color, highlightbackground=self.text_color, highlightcolor=self.text_color,
                                      highlightthickness=1)
        self.frame_top_three = tk.Frame(self.frame_top, bg=self.bgc_color, highlightbackground=self.text_color,
                                        highlightcolor=self.text_color, highlightthickness=1)

        self.frame_top_one.pack(side=tk.LEFT, padx=(98, 59), fill=tk.BOTH)
        self.frame_top_two.pack(side=tk.LEFT, padx=10, pady=5)
        self.frame_top_three.pack(side=tk.LEFT, padx=(61, 5), pady=5)

        self.frame_bot_left = tk.Frame(self.frame_bot, bg=self.bgc_color, highlightbackground=self.text_color, highlightcolor=self.text_color,
                                       highlightthickness=1)
        self.frame_bot_right = tk.Frame(self.frame_bot, bg=self.bgc_color, highlightbackground=self.text_color, highlightcolor=self.text_color,
                                        highlightthickness=1)
        self.frame_bot_left.pack(side=tk.LEFT, padx=5)
        self.frame_bot_right.pack(side=tk.LEFT, padx=5)

        # Frame top two internal frames
        self.frame_entry_container = tk.Frame(self.frame_top_two, bg=self.bgc_color)
        self.frame_entry_container.pack(side=tk.TOP, pady=3, fill=tk.BOTH)

        # Frame toolbar setup
        self.icon_close = tk.PhotoImage(file="../pictures/icon_close.png")
        self.button_close = tk.Button(self.frame_toolbar, image=self.icon_close, bg=self.light_bgc_color)
        self.button_close.pack(side=tk.LEFT, padx=5, pady=5)

        self.icon_accept = tk.PhotoImage(file="../pictures/icon_accept.png")
        self.button_add_recipe = tk.Button(self.frame_toolbar, image=self.icon_accept, bg=self.light_bgc_color)
        self.button_add_recipe.pack(side=tk.LEFT, padx=5, pady=5)

        self.icon_img = tk.PhotoImage(file="../pictures/icon_image.png")
        button_add_img = tk.Button(self.frame_toolbar, image=self.icon_img, bg=self.light_bgc_color,
                                   command=lambda: self.browse_files())
        button_add_img.pack(side=tk.LEFT, padx=5, pady=5)

        self.icon_plus = tk.PhotoImage(file="../pictures/icon_plus.png")
        button_open_ing_window = tk.Button(self.frame_toolbar, image=self.icon_plus, command=lambda: self.open_window(),
                                           bg=self.light_bgc_color)
        button_open_ing_window.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

        self.icon_minus = tk.PhotoImage(file="../pictures/icon_minus.png")
        button_del_ing = tk.Button(self.frame_toolbar, image=self.icon_minus,
                                   command=lambda: frame_methods.delete_ing_from_tree_view(self.tree_view_ingredients),
                                   bg=self.light_bgc_color)
        button_del_ing.pack(side=tk.RIGHT, padx=5, pady=5)

        # Frame top one setup
        self.img_path = "../pictures/no_image.png"
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img_food = ImageTk.PhotoImage(self.img)
        self.label_food_img = tk.Label(self.frame_top_one, image=self.img_food)
        self.label_food_img.pack(side=tk.LEFT, padx=5)

        # Frame top two setup
        entries_recipes_lab = 'Name:', 'Short desc:', 'Type:', 'Prep time:', 'Calories:'
        self.entries_recipes = frame_methods.make_entries(self, self.frame_entry_container, entries_recipes_lab)

        # Frame top three setup
        label_ingredients = tk.Label(self.frame_top_three, text="Ingredients", bg=self.light_bgc_color,
                                     font=self.helvetica_16, foreground=self.text_color)
        label_ingredients.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

        self.tree_view_ingredients, tree_view_scroll = frame_methods.create_ingredient_tree_view(self.frame_top_three)

        # Frame bot left setup
        label_desc = tk.Label(self.frame_bot_left, text="Description", bg=self.light_bgc_color,
                              font=self.helvetica_16, foreground=self.text_color)
        self.text_field_desc = tk.Text(self.frame_bot_left, width=60, height=10, bg=self.light_bgc_color,
                                       font=self.helvetica_12, selectbackground=self.clicked_bgc_color, foreground=self.text_color)
        label_desc.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)
        self.text_field_desc.pack(side=tk.LEFT, padx=5, pady=5)

        # Frame bot right setup
        label_inst = tk.Label(self.frame_bot_right, text="Instruction", bg=self.light_bgc_color, font=self.helvetica_16, foreground=self.text_color)
        self.text_field_inst = tk.Text(self.frame_bot_right, width=60, height=10, bg=self.light_bgc_color,
                                       font=self.helvetica_12, selectbackground=self.clicked_bgc_color, foreground=self.text_color)
        label_inst.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)
        self.text_field_inst.pack(side=tk.LEFT, padx=5, pady=5)

    def open_window(self):
        new_window = tk.Toplevel(self, bg=self.bgc_color)

        frame_window_entry_container = tk.Frame(new_window, bg=self.bgc_color)
        frame_window_entry_container.pack(side=tk.TOP, pady=3, fill=tk.BOTH)

        entries_ingredients_lab = 'Name:', 'Count:', 'Unit:'
        entries_ingredients = frame_methods.make_entries(self, frame_window_entry_container,
                                                         entries_ingredients_lab)

        button_add_ing_to_tree = tk.Button(new_window, text="ADD NEW", bg=self.light_bgc_color, font=self.helvetica_16,
                                           padx=10, bd=1, activebackground=self.clicked_bgc_color, foreground=self.text_color,
                                           command=lambda e=entries_ingredients:
                                           frame_methods.display_new_ing_in_tree_view(self.tree_view_ingredients, e))
        button_add_ing_to_tree.pack(side=tk.BOTTOM, padx=5, pady=5)

    def set_frame_info(self, name, short_desc, desc, ingredients, inst, meal_type, prep_time, calories, img_path):
        entries_values = [name, short_desc, meal_type, prep_time, calories]
        index = 0
        for entry in self.entries_recipes:
            frame_methods.set_entry_text(entry[1], entries_values[index])
            index += 1
        frame_methods.set_text_field_text(self.text_field_desc, desc)
        frame_methods.set_text_field_text(self.text_field_inst, inst)
        frame_methods.insert_to_ing_tree(self.tree_view_ingredients, ingredients)
        self.img_path = img_path
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img_food = ImageTk.PhotoImage(self.img)
        self.label_food_img.config(image=self.img_food)

    def browse_files(self):
        self.img_path = filedialog.askopenfilename(initialdir="/",
                                                   title="Select an img",
                                                   filetypes=[('image files', '.png'), ('image files2', '.jpg')])
        self.img = Image.open(self.img_path)
        self.img = self.img.resize((200, 200), Image.ANTIALIAS)
        self.img_food = ImageTk.PhotoImage(self.img)
        self.label_food_img.config(image=self.img_food)
