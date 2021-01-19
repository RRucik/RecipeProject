from Model.ingredient import Ingredient
from Model import exceptions


class IngredientList:

    def __init__(self):
        self.ingredient_list = []

    def add_ingredient(self, name, count, unit):
        in_list = any(ingredient.name == name for ingredient in self.ingredient_list)
        if in_list:
            raise exceptions.IngredientAlreadyStored('"{}" already in recipe!'.format(name))
        else:
            self.ingredient_list.append(Ingredient(name, count, unit))

    def read_ingredient(self, name):
        correct_ingredients = list(filter(lambda ingredient: ingredient.name == name, self.ingredient_list))
        if correct_ingredients:
            return correct_ingredients[0]
        else:
            raise exceptions.IngredientNotStored('"{}" is not in the recipe!'.format(name))

    def edit_ingredient(self, name, count, unit):
        indexed_ingredients = list(filter(lambda ingredient: ingredient[1].name == name,
                                          enumerate(self.ingredient_list)))
        if indexed_ingredients:
            index, ingredient_to_edit = indexed_ingredients[0][0], indexed_ingredients[0][1]
            self.ingredient_list[index].count = count
            self.ingredient_list[index].unit = unit
        else:
            raise exceptions.IngredientNotStored('"{}" is not in the recipe!'.format(name))

    def delete_ingredient(self, name):
        indexed_ingredients = list(filter(lambda ingredient: ingredient[1].name == name,
                                          enumerate(self.ingredient_list)))
        if indexed_ingredients:
            index, ingredient_to_edit = indexed_ingredients[0][0], indexed_ingredients[0][1]
            del self.ingredient_list[index]
        else:
            raise exceptions.IngredientNotStored('"{}" is not in the recipe!'.format(name))

    @property
    def ingredient_list(self):
        return self.__ingredient_list

    @ingredient_list.setter
    def ingredient_list(self, new_ingredient_list):
        self.__ingredient_list = new_ingredient_list


# il = IngredientList()
# il.add_ingredient("Tomato", -1, "units")
# il.add_ingredient("Olive oil", 1, "tbs")
# il.add_ingredient("Mozarella", 1, "kg")
# il.add_ingredient("Bazil", 1, "leaf")
# il.display()
# il.edit_ingredient("Tomato", 5, "kg")
# il.display()
