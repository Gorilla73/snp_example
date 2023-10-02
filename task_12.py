class Dessert:

    def __init__(self, name=None, calories=None):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def get_calories(self):
        return self.calories

    def set_name(self, name):
        self.name = name
        return

    def set_calories(self, calories):
        self.calories = calories
        return

    def is_healthy(self):

        try:
            if (type(self.calories) != int) and (type(self.calories) != float):
                raise TypeError
        except TypeError:
            return "TypeError: Ожидался float или int"
        else:

            if self.calories < 200:
                return True
            return False

    def is_delicious(self):
        return True

class JellyBean(Dessert):

    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self.flavor = flavor

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, flavor):
        self.flavor = flavor

    def is_delicious(self):
        if self.flavor == "black licorice":
            return False
        return True


