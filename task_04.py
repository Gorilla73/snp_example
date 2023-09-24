import unittest

def sort_list(l):

    if l == []:
        return []

    maximum = max(l)
    minimum = min(l)

    for i in range(len(l)):

        if l[i] == minimum:
            l[i] = maximum

        elif l[i] == maximum:
            l[i] = minimum

    l.append(minimum)
    return l


class TestTask04(unittest.TestCase):

    def test1(self):
        self.assertEqual(sort_list([]), [])

    def test2(self):
        self.assertEqual(sort_list([2, 4, 6, 8]), [8, 4, 6, 2, 2])

    def test3(self):
        self.assertEqual(sort_list([1]), [1, 1])

    def test4(self):
        self.assertEqual(sort_list([1, 2, 1, 3]), [3, 2, 3, 1, 1])
