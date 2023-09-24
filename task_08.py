def multiply_numbers(inputs=None):

    result = 1
    count_digit = 0

    if inputs is None:
        return None

    if (type(inputs)) != str:
        if type(inputs) == list:
            inputs = "".join(str(el) for el in inputs)
        elif (type(inputs) == float) or (type(inputs) == int):
            inputs = str(inputs)
        else:
            raise "Несовместимый тип данных"

    for i in range(len(inputs)):
        if inputs[i].isdigit():
            result *= int(inputs[i])
            count_digit += 1

    if count_digit == 0:
        return None

    return result


print(multiply_numbers()) # => None
print(multiply_numbers('ss')) # => None
print(multiply_numbers('1234')) # => 24
print(multiply_numbers('sssdd34')) # => 12
print(multiply_numbers(2.3)) # => 6
print(multiply_numbers([5, 6, 4])) # => 120

