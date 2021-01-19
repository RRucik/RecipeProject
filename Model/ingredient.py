class Ingredient:

    def __init__(self, name, count, unit):
        self.name = name
        self.count = count
        self.unit = unit

    @property
    def name(self):
        return self.__name

    @property
    def count(self):
        return self.__count

    @property
    def unit(self):
        return self.__unit

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @count.setter
    def count(self, new_count):
        if new_count <= 0:
            raise ValueError("Ingredient count below or equal to 0")
        self.__count = new_count

    @unit.setter
    def unit(self, new_unit):
        self.__unit = new_unit

    def __str__(self):
        return "{} {} {}".format(self.name, self.count, self.unit)
