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

        try:
            if type(self.__calories) != int:
                raise TypeError
        except TypeError:
            print("TypeError: Ожидался тип int")
        else:

            if self.__calories < 200:
                return True
            return False

    def is_delicious(self):
        return True


dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2":
    raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
dessert.calories = "test_calories2"
print(dessert.calories)
if dessert.calories != "test_calories2":
    raise Exception("Setter for calorues is not working")
print(dessert.is_delicious())
if not dessert.is_delicious():
    raise Exception("Invalid method result")
print(dessert.is_healthy())