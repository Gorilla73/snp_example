def combine_anagrams(words_array):

    words_array = [word.lower() for word in words_array]

    d = {}
    for w in words_array:
        sorted_w = ''.join(sorted(w))

        if sorted_w not in d:
            d[sorted_w] = [w]
        else:
            d[sorted_w].append(w)

    return [value for value in d.values()]



print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
# => [ ["cars", "racs", "scar"], ["four"], ["for"],["potatoes"], ["creams", "scream"]]