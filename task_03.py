import unittest

def max_odd(array):

    array = [int(el) for el in array if type(el) == int or type(el) == float]
    array = [el for el in array if el % 2 != 0]

    if array == []:
        return None
    return max(array)


class TestTask03(unittest.TestCase):

    def test1(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)

    def test2(self):
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)

    def test3(self):
        self.assertEqual(max_odd(['ololo', 2, 3, 4, [1, 2], None]), 3)

    def test4(self):
        self.assertEqual(max_odd(['ololo', 'fufufu']), None)

    def test5(self):
        self.assertEqual(max_odd([2, 2, 4]), None)


# class TestTask01(unittest.TestCase):
#
#     def test1(self):
#         self.assertEqual()
#
#     def test2(self):
#         self.assertEqual()
#
#     def test3(self):
#         self.assertEqual()
#
#     def test4(self):
#         self.assertEqual()
#
#     def test5(self):
#         self.assertEqual()