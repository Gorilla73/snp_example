class Dessert:

    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    def get_name(self):
        return self.__name

    def get_calories(self):
        return self.__calories

    def set_name(self, name):
        self.__name = name
        return

    def set_calories(self, calories):
        self.__calories = calories
        return

    def is_healthy(self):
        if self.__calories < 200:
            return True
        return False

    def is_delicious(self):
        return True