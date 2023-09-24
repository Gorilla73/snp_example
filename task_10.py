import re

def count_words(string):

    l = re.sub("[^A-Za-z0-9\s]", "", str(string)).lower().split()

    res_d = {}

    for el in l:
        if el not in res_d:
            res_d[el] = 1
        else:
            res_d[el] += 1

    return res_d


print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
print(count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}