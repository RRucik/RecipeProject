import tkinter as tk

from PIL import ImageTk
from PIL import Image
from View import frame_custom
from View import frame_methods


class FrameSelect(frame_custom.FrameCustom):

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
        self.frame_top_two = tk.Frame(self.frame_top, bg=self.bgc_color, highlightbackground=self.text_color,
                                      highlightthickness=1)
        self.frame_top_three = tk.Frame(self.frame_top, bg=self.bgc_color, highlightbackground=self.text_color,
                                        highlightcolor=self.text_color, highlightthickness=1)

        self.frame_top_one.pack(side=tk.LEFT, padx=(98, 16), fill=tk.BOTH)
        self.frame_top_two.pack(side=tk.LEFT, padx=10, pady=5)
        self.frame_top_three.pack(side=tk.LEFT, padx=(18, 5), pady=5)

        self.frame_bot_left = tk.Frame(self.frame_bot, bg=self.bgc_color, highlightbackground=self.text_color,
                                       highlightthickness=1)
        self.frame_bot_right = tk.Frame(self.frame_bot, bg=self.bgc_color, highlightbackground=self.text_color,
                                        highlightthickness=1)
        self.frame_bot_left.pack(side=tk.LEFT, padx=5)
        self.frame_bot_right.pack(side=tk.LEFT, padx=5)

        # Frame top two internal frames
        self.title_frame = tk.Frame(self.frame_top_two, bg=self.bgc_color)
        self.base_info_frame = tk.Frame(self.frame_top_two, bg=self.bgc_color)
        self.title_frame.pack(side=tk.TOP, padx=10, pady=(13, 10))
        self.base_info_frame.pack(side=tk.BOTTOM, padx=10, pady=(5, 25))

        # Frame toolbar setup
        self.icon_close = tk.PhotoImage(file="../pictures/icon_close.png")
        self.button_close = tk.Button(self.frame_toolbar, image=self.icon_close, bg=self.light_bgc_color)
        self.button_close.pack(side=tk.LEFT, padx=5, pady=5)

        self.icon_edit = tk.PhotoImage(file="../pictures/icon_edit.png")
        self.button_edit = tk.Button(self.frame_toolbar, image=self.icon_edit, bg=self.light_bgc_color)
        self.button_edit.pack(side=tk.LEFT, padx=5, pady=5)

        self.icon_delete = tk.PhotoImage(file="../pictures/icon_delete.png")
        self.button_delete = tk.Button(self.frame_toolbar, image=self.icon_delete, bg=self.light_bgc_color)
        self.button_delete.pack(side=tk.LEFT, padx=5, pady=5)

        # Frame top one setup
        self.img_path = "../pictures/no_image.png"
        self.img_food = tk.PhotoImage(file=self.img_path)
        self.label_food_img = tk.Label(self.frame_top_one, image=self.img_food, foreground=self.text_color)
        self.label_food_img.pack(side=tk.LEFT, padx=5)

        # Frame top two setup
        self.label_name = tk.Label(self.title_frame, text="", width=22, bg=self.bgc_color, font=self.helvetica_24, foreground=self.text_color)
        self.label_short_desc = tk.Label(self.title_frame, text="", bg=self.bgc_color, font=self.helvetica_24, foreground=self.text_color)
        self.label_name.pack(side=tk.TOP, padx=5, pady=10)
        self.label_short_desc.pack(side=tk.TOP, padx=5, pady=10)

        self.label_type = tk.Label(self.base_info_frame, text="", bg=self.bgc_color, font=self.helvetica_16, foreground=self.text_color)
        self.label_prep_time = tk.Label(self.base_info_frame, text="", bg=self.bgc_color,
                                        font=self.helvetica_16, foreground=self.text_color)
        self.label_calories = tk.Label(self.base_info_frame, text="", bg=self.bgc_color,
                                       font=self.helvetica_16, foreground=self.text_color)
        self.label_type.pack(side=tk.LEFT, padx=10)
        self.label_prep_time.pack(side=tk.LEFT, padx=10)
        self.label_calories.pack(side=tk.LEFT, padx=10)

        # Frame top three setup
        label_ingredients = tk.Label(self.frame_top_three, text="Ingredients", bg=self.light_bgc_color, foreground=self.text_color,
                                     font=self.helvetica_16)
        label_ingredients.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)

        self.tree_view_ingredients, tree_view_scroll = frame_methods.create_ingredient_tree_view(self.frame_top_three)

        # Frame bot left setup
        label_desc = tk.Label(self.frame_bot_left, text="Description", bg=self.light_bgc_color, font=self.helvetica_16, foreground=self.text_color)
        self.label_desc_detailed = tk.Label(self.frame_bot_left, width=60, height=10, text="Desc", justify="left",
                                            bg=self.light_bgc_color, wraplength=520, font=self.helvetica_12, foreground=self.text_color)
        label_desc.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)
        self.label_desc_detailed.pack(side=tk.LEFT, padx=5, pady=5)

        # Frame bot right setup
        label_inst = tk.Label(self.frame_bot_right, text="Instruction", bg=self.light_bgc_color, font=self.helvetica_16, foreground=self.text_color)
        self.label_inst_detailed = tk.Label(self.frame_bot_right, width=60, height=10, text="Inst", justify="left",
                                            bg=self.light_bgc_color, wraplength=520, font=self.helvetica_12, foreground=self.text_color)
        label_inst.pack(side=tk.TOP, padx=5, pady=5, fill=tk.BOTH)
        self.label_inst_detailed.pack(side=tk.LEFT, padx=5, pady=5)

    def set_select_frame_info(self, name, short_desc, desc, ing, inst, meal_type, prep_time, calories, img_path):
        self.label_name.config(text=name)
        self.label_short_desc.config(text=short_desc)
        self.label_desc_detailed.config(text=desc)
        self.label_inst_detailed.config(text=inst)
        self.label_type.config(text="Type: " + meal_type)
        self.label_prep_time.config(text="Prep time: " + str(prep_time))
        self.label_calories.config(text="Cal: " + str(calories))
        self.tree_view_ingredients.delete(*self.tree_view_ingredients.get_children())
        self.img_path = img_path
        new_img = Image.open(self.img_path)
        new_img = new_img.resize((200, 200), Image.ANTIALIAS)
        self.img_food = ImageTk.PhotoImage(new_img)
        self.label_food_img.config(image=self.img_food)

        self.label_food_img.config(image=self.img_food)
        for ingredient in ing:
            self.tree_view_ingredients.insert(parent='', index='end', iid=ingredient.name, text="",
                                              values=(ingredient.name.lower(), ingredient.count, ingredient.unit))
