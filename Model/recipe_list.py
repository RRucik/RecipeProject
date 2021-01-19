import pickle

from Model.recipe import Recipe
from Model import exceptions


class RecipeList:

    def __init__(self):
        self.recipe_list = []

    def add_recipe(self, name, short_desc, desc, ingredients, inst, meal_type, prep_time, calories, img):
        in_list = any(recipe.name == name for recipe in self.recipe_list)
        if in_list:
            raise exceptions.RecipeAlreadyStored('"{}" recipe has been already created'.format(name))
        else:
            self.recipe_list.append(Recipe(name, short_desc, desc, ingredients, inst, meal_type, prep_time, calories, img))

    def read_recipe(self, name):
        correct_recipes = list(filter(lambda recipe: recipe.name == name, self.recipe_list))
        if correct_recipes:
            return correct_recipes[0]
        else:
            raise exceptions.RecipeNotStored('"{}" recipe does not exist'.format(name))

    def edit_recipe(self, name_old, name_new, short_desc, desc, ingredients, inst, meal_type, prep_time, calories, img):
        indexed_recipes = list(filter(lambda recipe: recipe[1].name == name_old, enumerate(self.recipe_list)))
        new_name_already_in_recipes = list(filter(lambda recipe: recipe.name == name_new, self.recipe_list))
        if not indexed_recipes:
            raise exceptions.RecipeNotStored('"{}" recipe does not exist'.format(name_old))
        elif new_name_already_in_recipes and name_new != name_old:
            raise exceptions.RecipeAlreadyStored('"{}" recipe has been already created'.format(name_new))
        else:
            index, recipe_to_edit = indexed_recipes[0][0], indexed_recipes[0][1]
            self.recipe_list[index].name = name_new
            self.recipe_list[index].short_desc = short_desc
            self.recipe_list[index].desc = desc
            self.recipe_list[index].ingredients = ingredients
            self.recipe_list[index].inst = inst
            self.recipe_list[index].meal_type = meal_type
            self.recipe_list[index].prep_time = prep_time
            self.recipe_list[index].calories = calories
            self.recipe_list[index].img = img

    def delete_recipe(self, name):
        indexed_recipes = list(filter(lambda recipe: recipe[1].name == name, enumerate(self.recipe_list)))
        if indexed_recipes:
            index, recipe_to_edit = indexed_recipes[0][0], indexed_recipes[0][1]
            del self.recipe_list[index]
        else:
            raise exceptions.RecipeNotStored('"{}" recipe does not exist'.format(name))

    def filter_recipe_list(self, part_of_name=None, meal_type=None, min_cal=None, max_cal=None, prep_time_min=None,
                           prep_time_max=None):
        filtered_recipes = []
        for recipe in self.recipe_list:
            if (part_of_name is None or part_of_name.lower() in recipe.name.lower()) \
                    and (meal_type is None or meal_type.lower() in recipe.meal_type.lower()) \
                    and (min_cal is None or recipe.calories >= int(min_cal)) \
                    and (max_cal is None or recipe.calories <= int(max_cal)) \
                    and (prep_time_min is None or recipe.prep_time >= int(prep_time_min)) \
                    and (prep_time_max is None or recipe.prep_time <= int(prep_time_max)):
                filtered_recipes.append(recipe)
        return filtered_recipes

    @classmethod
    def load_recipe_list(cls, file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)

    def save_recipe_list(self, file_path):
        with open(file_path, 'wb') as file:
            return pickle.dump(self, file)

    @property
    def recipe_list(self):
        return self.__recipe_list

    @recipe_list.setter
    def recipe_list(self, new_recipe_list):
        self.__recipe_list = new_recipe_list
