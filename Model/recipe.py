class Recipe:

    def __init__(self, name, short_desc, desc, ingredients, inst, meal_type, prep_time, calories, img):
        self.name = name
        self.short_desc = short_desc
        self.desc = desc
        self.ingredients = ingredients
        self.inst = inst
        self.meal_type = meal_type
        self.prep_time = prep_time
        self.calories = calories
        self.img = img

    def add_ingredient_to_recipe(self, name, count, unit):
        self.ingredients.add_ingredient(name, count, unit)

    def read_ingredient_in_recipe(self, name):
        self.ingredients.read_ingredient(name)

    def edit_ingredient_in_recipe(self, name, count, unit):
        self.ingredients.edit_ingredient(name, count, unit)

    def delete_ingredient_from_recipe(self, name):
        self.ingredients.delete_ingredient(name)

    @property
    def name(self):
        return self.__name

    @property
    def short_desc(self):
        return self.__short_desc

    @property
    def desc(self):
        return self.__desc

    @property
    def ingredients(self):
        return self.__ingredients

    @property
    def inst(self):
        return self.__inst

    @property
    def meal_type(self):
        return self.__meal_type

    @property
    def prep_time(self):
        return self.__prep_time

    @property
    def calories(self):
        return self.__calories

    @property
    def img(self):
        return self.__img

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @short_desc.setter
    def short_desc(self, new_short_desc):
        self.__short_desc = new_short_desc

    @desc.setter
    def desc(self, new_desc):
        self.__desc = new_desc

    @ingredients.setter
    def ingredients(self, new_ingredients):
        self.__ingredients = new_ingredients

    @inst.setter
    def inst(self, new_inst):
        self.__inst = new_inst

    @meal_type.setter
    def meal_type(self, new_meal_type):
        self.__meal_type = new_meal_type

    @prep_time.setter
    def prep_time(self, new_prep_time):
        self.__prep_time = new_prep_time

    @calories.setter
    def calories(self, new_calories):
        self.__calories = new_calories

    @img.setter
    def img(self, new_img):
        self.__img = new_img

    def __str__(self):
        return "{}{}{}{}" \
            .format(self.name, self.meal_type, self.prep_time, self.calories)
