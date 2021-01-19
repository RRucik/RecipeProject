from Model.ingredient_list import IngredientList
from Model.recipe_list import RecipeList
from View.view import View


class Controller:

    def __init__(self):
        self.model = RecipeList()
        self.view = View()

        self.frame_select = self.view.frames["FrameSelect"]
        self.frame_search = self.view.frames["FrameSearch"]
        self.frame_add = self.view.frames["FrameAdd"]
        self.frame_edit = self.view.frames["FrameEdit"]
        self.bind_buttons()

    def run(self):
        self.view.configure_gui()
        self.change_frame_to_search()
        self.view.start_gui()

    def change_frame_to_search(self):
        self.frame_search.tkraise()

    def change_frame_to_add(self):
        self.frame_add.tkraise()

    def change_frame_to_select(self):
        recipe_name = self.view.get_selected_name(self.frame_search.tree_view_recipes)
        if recipe_name != "":
            recipe = self.model.read_recipe(recipe_name)
            self.frame_select.set_select_frame_info(recipe.name, recipe.short_desc, recipe.desc,
                                                    recipe.ingredients.ingredient_list, recipe.inst,
                                                    recipe.meal_type, recipe.prep_time, recipe.calories, recipe.img)
            self.frame_select.tkraise()

    def change_frame_to_edit(self, recipe_name):
        recipe = self.model.read_recipe(recipe_name)
        self.frame_edit.set_frame_info(recipe.name, recipe.short_desc, recipe.desc,
                                       recipe.ingredients.ingredient_list, recipe.inst, recipe.meal_type,
                                       recipe.prep_time, recipe.calories, recipe.img)
        self.frame_edit.tkraise()

    def add_recipe(self, entries, tree_view, text_view_desc, text_view_inst, img_path):
        fields_dict = self.view.get_data_from_entries(entries)
        ing_list = self.view.get_data_from_tree_view(tree_view)
        desc_text = self.view.get_data_from_text_view(text_view_desc)
        inst_text = self.view.get_data_from_text_view(text_view_inst)
        i = IngredientList()
        for ing in ing_list:
            i.add_ingredient(name=ing[0], count=int(ing[1]), unit=ing[2])

        self.model.add_recipe(name=fields_dict['Name:'],
                              short_desc=fields_dict['Short desc:'],
                              meal_type=fields_dict['Type:'],
                              calories=int(fields_dict['Calories:']),
                              prep_time=int(fields_dict['Prep time:']),
                              desc=desc_text,
                              inst=inst_text,
                              ingredients=i,
                              img=img_path)

    def delete_recipe(self, name):
        self.model.delete_recipe(name)
        self.change_frame_to_search()
        self.view.clear_tree_view(self.frame_search.tree_view_recipes)

    def update_recipe(self, name, entries, tree_view, text_view_desc, text_view_inst, img_path):
        fields_dict = self.view.get_data_from_entries(entries)
        ing_list = self.view.get_data_from_tree_view(tree_view)
        desc_text = self.view.get_data_from_text_view(text_view_desc)
        inst_text = self.view.get_data_from_text_view(text_view_inst)
        i = IngredientList()
        for ing in ing_list:
            i.add_ingredient(name=ing[0], count=int(ing[1]), unit=ing[2])
        self.model.edit_recipe(name_old=name,
                               name_new=fields_dict['Name:'],
                               short_desc=fields_dict['Short desc:'],
                               meal_type=fields_dict['Type:'],
                               calories=int(fields_dict['Calories:']),
                               prep_time=int(fields_dict['Prep time:']),
                               desc=desc_text,
                               inst=inst_text,
                               ingredients=i,
                               img=img_path)
        self.change_frame_to_search()
        self.view.clear_tree_view(self.frame_search.tree_view_recipes)

    def find_filtered_recipes(self, entries, tree_view):
        fields_dict = self.view.get_data_from_entries(entries)
        filtered_recipes = RecipeList()
        filtered_recipes.recipe_list = self.model.filter_recipe_list(part_of_name=fields_dict['Part of name:'],
                                                                     meal_type=fields_dict['Meal type:'],
                                                                     min_cal=fields_dict['Min calories:'],
                                                                     max_cal=fields_dict['Max calories:'],
                                                                     prep_time_min=fields_dict['Prep time min:'],
                                                                     prep_time_max=fields_dict['Prep time max:'])
        self.view.insert_to_recipe_tree(tree_view, filtered_recipes.recipe_list)

    def save_recipe_list(self):
        self.model.save_recipe_list("../Model/data")

    def load_recipe_list(self):
        self.model = self.model.load_recipe_list("../Model/data")

    def bind_buttons(self):
        self.frame_search.button_add.bind('<Button-1>', lambda event: self.change_frame_to_add())
        self.frame_search.button_search.bind('<Button-1>',
                                             lambda event, e=self.frame_search.entries: self.find_filtered_recipes(
                                                 e, self.frame_search.tree_view_recipes))
        self.frame_search.button_select.bind('<Button-1>', lambda event: self.change_frame_to_select())

        self.frame_select.button_close.bind('<Button-1>', lambda event: self.change_frame_to_search())
        self.frame_select.button_edit.bind('<Button-1>', lambda event: self.change_frame_to_edit(
            self.frame_select.label_name.cget("text")))
        self.frame_select.button_delete.bind('<Button-1>', lambda event: self.delete_recipe(
            self.frame_select.label_name.cget("text")))

        self.frame_add.button_close.bind('<Button-1>', lambda event: self.change_frame_to_search())
        self.frame_add.button_add_recipe.bind('<Button-1>',
                                              lambda event, e=self.frame_add.entries_recipes,
                                                     tv=self.frame_add.tree_view_ingredients,
                                                     t1=self.frame_add.text_field_desc,
                                                     t2=self.frame_add.text_field_inst:
                                                     self.add_recipe(e, tv, t1, t2, self.frame_add.img_path))

        self.frame_edit.button_close.bind('<Button-1>', lambda event: self.change_frame_to_search())
        self.frame_edit.button_add_recipe.bind('<Button-1>',
                                               lambda event, e=self.frame_edit.entries_recipes,
                                                      tv=self.frame_edit.tree_view_ingredients,
                                                      t1=self.frame_edit.text_field_desc,
                                                      t2=self.frame_edit.text_field_inst:
                                                        self.update_recipe(self.frame_select.label_name.cget("text"), e,
                                                                           tv,  t1, t2, self.frame_edit.img_path))
        self.view.menu.add_command(label="Save", command=self.save_recipe_list)
        self.view.menu.add_command(label="Load", command=self.load_recipe_list)


c = Controller()
c.run()
