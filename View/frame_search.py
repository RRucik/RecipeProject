import tkinter as tk
from View import frame_custom, frame_methods


class FrameSearch(frame_custom.FrameCustom):

    def __init__(self, parent):
        frame_custom.FrameCustom.__init__(self, parent)

        # Frames setup
        self.left_frame = tk.Frame(self, bg=self.bgc_color)
        self.right_frame = tk.Frame(self, bg=self.bgc_color, highlightbackground=self.text_color,
                                    highlightcolor=self.text_color, highlightthickness=1)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.right_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.right_frame_top = tk.Frame(self.right_frame, bg=self.bgc_color)
        self.right_frame_bot = tk.Frame(self.right_frame, bg=self.bgc_color)
        self.right_frame_top.pack(side=tk.TOP, padx=90, pady=10)
        self.right_frame_bot.pack(side=tk.BOTTOM, padx=10, pady=15)

        # Left frame setup
        self.tree_view_recipes, tree_view_scroll = frame_methods.create_recipe_tree_view(self.left_frame)

        # Right frame top setup
        filter_label = tk.Label(self.right_frame_top, text="FILTER BY", width=12, bg=self.bgc_color,
                                font=self.helvetica_24, foreground=self.text_color)
        filter_label.pack(side=tk.TOP, padx=5, pady=20)
        entries_labels_names = 'Part of name:', 'Meal type:', 'Min calories:', 'Max calories:', \
                               'Prep time min:', 'Prep time max:'
        self.entries = frame_methods.make_entries(self, self.right_frame_top, entries_labels_names)

        # Right frame bot setup
        self.button_search = tk.Button(self.right_frame_bot, text='SEARCH', bg=self.light_bgc_color,
                                       foreground=self.text_color, activeforeground=self.text_color,
                                       font=self.helvetica_16, padx=10, bd=1, activebackground=self.clicked_bgc_color)
        self.button_select = tk.Button(self.right_frame_bot, text="SELECT", bg=self.light_bgc_color,
                                       foreground=self.text_color, activeforeground=self.text_color,
                                       font=self.helvetica_16, padx=10, bd=1, activebackground=self.clicked_bgc_color)
        self.button_add = tk.Button(self.right_frame_bot, text="ADD NEW", bg=self.light_bgc_color,
                                    foreground=self.text_color, activeforeground=self.text_color,
                                    font=self.helvetica_16, padx=10, bd=1, activebackground=self.clicked_bgc_color)

        self.button_search.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_select.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_add.pack(side=tk.LEFT, padx=10, pady=5)

