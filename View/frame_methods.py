import tkinter as tk
from tkinter import ttk
from tkinter.font import Font


# Methods for creating frame elements
def make_entries(frame, root_frame, labels_names):
    my_entries = []
    for label_name in labels_names:
        entry_container = tk.Frame(root_frame, bg=frame.bgc_color)
        label = tk.Label(entry_container, text=label_name, width=12, bg=frame.bgc_color, font=frame.helvetica_16,
                         foreground=frame.text_color, anchor="w")
        entry = tk.Entry(entry_container, width=15, bg=frame.light_bgc_color, font=frame.helvetica_16,
                         foreground=frame.text_color, selectbackground=frame.clicked_bgc_color)
        entry_container.pack(side=tk.TOP)
        label.pack(side=tk.LEFT, padx=5, pady=5)
        entry.pack(side=tk.RIGHT, padx=(15, 5), pady=5)
        my_entries.append((label_name, entry))
    return my_entries


def create_recipe_tree_view(root_frame):
    tree_view_scroll = ttk.Scrollbar(root_frame, style="TScrollbar")
    tree_view_recipes = ttk.Treeview(root_frame, height=15, style="Custom.Treeview",
                                     selectmode="browse", yscrollcommand=tree_view_scroll.set)
    tree_view_recipes["columns"] = ("one", "two", "three", "four")
    tree_view_recipes.column("#0", width=0, stretch=tk.NO)
    tree_view_recipes.column("one", width=150, minwidth=150, stretch=tk.NO)
    tree_view_recipes.column("two", width=150, minwidth=150, stretch=tk.NO)
    tree_view_recipes.column("three", width=120, minwidth=120, stretch=tk.NO)
    tree_view_recipes.column("four", width=120, minwidth=120, stretch=tk.NO)
    tree_view_recipes.heading("#0", text="ID", anchor=tk.W)
    tree_view_recipes.heading("one", text="NAME", anchor=tk.W)
    tree_view_recipes.heading("two", text="TYPE", anchor=tk.W)
    tree_view_recipes.heading("three", text="PREP TIME", anchor=tk.W)
    tree_view_recipes.heading("four", text="CALORIES", anchor=tk.W)
    tree_view_scroll.config(command=tree_view_recipes.yview)
    tree_view_recipes.pack(side=tk.LEFT, padx=5, pady=5)
    tree_view_scroll.pack(side=tk.LEFT, fill=tk.Y)
    return tree_view_recipes, tree_view_scroll


def create_ingredient_tree_view(root_frame):
    tree_view_scroll = ttk.Scrollbar(root_frame, style="TScrollbar")
    tree_view_ingredients = ttk.Treeview(root_frame, height=5, style="Custom.Treeview", selectmode="browse",
                                         yscrollcommand=tree_view_scroll.set)
    tree_view_ingredients["columns"] = ("one", "two", "three")
    tree_view_ingredients.column("#0", width=0, stretch=tk.NO)
    tree_view_ingredients.column("one", width=120, minwidth=120, stretch=tk.NO)
    tree_view_ingredients.column("two", width=80, minwidth=80, stretch=tk.NO)
    tree_view_ingredients.column("three", width=80, minwidth=80, stretch=tk.NO)
    tree_view_ingredients.heading("#0", text="ID", anchor=tk.W)
    tree_view_ingredients.heading("one", text="NAME", anchor=tk.W)
    tree_view_ingredients.heading("two", text="COUNT", anchor=tk.W)
    tree_view_ingredients.heading("three", text="UNIT", anchor=tk.W)
    tree_view_scroll.config(command=tree_view_ingredients.yview)
    tree_view_ingredients.pack(side=tk.LEFT, padx=5, pady=5)
    tree_view_scroll.pack(side=tk.LEFT, fill=tk.Y)

    return tree_view_ingredients, tree_view_scroll


# Methods for displaying data in view elements
def set_entry_text(entry, text):
    entry.delete(0, tk.END)
    entry.insert(0, text)


def set_text_field_text(text_field, text):
    text_field.delete("1.0", tk.END)
    text_field.insert("1.0", text)


def display_new_ing_in_tree_view(tree_view, entries):
    fields_dict = get_data_from_entries(entries)
    if None not in fields_dict.values():
        tree_view.insert(parent='', index='end', iid=fields_dict['Name:'], text="",
                         values=(fields_dict['Name:'], fields_dict['Count:'], fields_dict['Unit:']))


def delete_ing_from_tree_view(tree_view):
    tree_view.delete(get_selected_from_tree(tree_view))


def clear_tree_view(tree_view):
    tree_view.delete(*tree_view.get_children())


def insert_to_recipes_tree(tree_view, recipe_list):
    tree_view.delete(*tree_view.get_children())
    for recipe in recipe_list:
        tree_view.insert(parent='', index='end', iid=recipe.name, text="",
                         values=(recipe.name.lower(), recipe.meal_type.lower(), recipe.prep_time, recipe.calories))


def insert_to_ing_tree(tree_view, ing_list):
    tree_view.delete(*tree_view.get_children())
    for ingredient in ing_list:
        tree_view.insert(parent='', index='end', iid=ingredient.name, text="",
                         values=(ingredient.name.lower(), ingredient.count, ingredient.unit))


# Methods for getting data from view elements
def get_data_from_entries(entries):
    fields_dict = {}
    for entry in entries:
        entry_val = entry[1].get()
        if entry_val == "":
            fields_dict[entry[0]] = None
        else:
            fields_dict[entry[0]] = entry_val
    return fields_dict


def get_data_from_text_view(text_view):
    text = text_view.get("1.0", tk.END)
    if text == "":
        return None
    return text


def get_selected_from_tree(tree_view):
    return tree_view.focus()


def get_data_from_tree(tree_view):
    tree_records = []
    for idd in tree_view.get_children():
        tree_records.append(tree_view.item(idd)['values'])
    return tree_records


# Set gui style
def set_style():
    bgc_color = "#5F5980"
    light_bgc_color = "#756F9B"
    clicked_bgc_color = "#807BA3"
    text_color = "#FFFFFF"

    helvetica_12 = Font(family="Helvetica", size="12")

    style = ttk.Style()
    style.theme_use("clam")

    style.element_create("Custom.Treeheading.border", "from", "default")
    style.layout("Custom.Treeview.Heading", [
        ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
        ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                ("Custom.Treeheading.text", {'sticky': 'we'})
            ]})
        ]}),
    ])
    style.configure("Custom.Treeview.Heading",
                    background=bgc_color, foreground=text_color, relief="groove", font=helvetica_12)
    style.map("Custom.Treeview.Heading", background=[('selected', bgc_color)])

    style.configure("Custom.Treeview", background=light_bgc_color, fieldbackground=light_bgc_color,
                    bordercolor="black", foreground=text_color, rowheight=25, font=helvetica_12)
    style.map("Custom.Treeview", background=[('selected', clicked_bgc_color)], foreground=[('selected', text_color)])

    style.configure("TScrollbar", gripcount=0,
                    background=light_bgc_color, darkcolor=light_bgc_color, lightcolor=light_bgc_color,
                    troughcolor=clicked_bgc_color, bordercolor=text_color, arrowcolor=text_color)

    style.map("TScrollbar", background=[('selected', bgc_color)])


def set_app_background(app, bgc_path):
    app.background_image = tk.PhotoImage(file=bgc_path)
    background_label = tk.Label(app, image=app.background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
