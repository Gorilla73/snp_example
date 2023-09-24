import unittest

def coincidence(list = None, range = None):

    result = []
    if (list is None or range is None):
        return []

    for el in list:
        if type(el) == float:
            new_el = int(el)
        else:
            new_el = el

        if new_el in range:
            result.append(el)

    return result


class TestTask02(unittest.TestCase):

    def test1(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5], range(3, 6)), [3, 4, 5])

    def test2(self):
        self.assertEqual(coincidence(), [])

    def test3(self):
        self.assertEqual(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)), [1, 2, 2.5])


