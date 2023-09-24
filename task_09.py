def connect_dicts(dict1, dict2):
    res_d = {}

    sum_d1 = sum(dict1.values())
    sum_d2 = sum(dict2.values())

    if sum_d1 > sum_d2:
        for key, value in dict1.items():
            if value >= 10:
                res_d[key] = value

        for key, value in dict2.items():
            if key not in res_d:
                if value >= 10:
                    res_d[key] = value

    else:
        for key, value in dict2.items():
            if value >= 10:
                res_d[key] = value

        for key, value in dict1.items():
            if key not in res_d:
                if value >= 10:
                    res_d[key] = value

    return dict(sorted(res_d.items(), key=lambda item: item[1]))




print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))  # => {"c": 11, "b": 12}
print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))  # => {d: 11, "c": 12, "a": 13}
print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))  # => {"c": 11, "b": 12, "a": 15}