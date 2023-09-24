import re
import unittest


def is_palindrome(string):
    if (type(string) == None):
        return False

    good_string = re.sub("[^A-Za-z0-9]", "", str(string)).lower()

    return good_string == good_string[::-1]


is_palindrome("A man, a plan, a canal -- Panama")  # => True
is_palindrome("Madam, I'm Adam!")  # => True
is_palindrome(333)  # => True
is_palindrome(None)  # => False
is_palindrome("Abracadabra")  # => False


class TestTask01(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal -- Panama"), True)

    def test2(self):
        self.assertEqual(is_palindrome("Madam, I'm Adam!"), True)

    def test3(self):
        self.assertEqual(is_palindrome(333), True)

    def test4(self):
        self.assertEqual(is_palindrome(None), False)

    def test5(self):
        self.assertEqual(is_palindrome("Abracadabra"), False)

