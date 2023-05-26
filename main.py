result = []


def divider(a, b):
    if type(a) != int:
        raise TypeError

    elif a < b:
        raise ValueError

    elif b > 100:
        raise IndexError

    elif b == 0:
        raise ZeroDivisionError

    return a / b


data = {10: 2, 1: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)

# def checker(a):
#     if type(a) != str:
#         raise TypeError(f"Sorry, we can't work with {type(a),}, we need class str")
#     else:
#         return a
#
#
# var = 10
# checker(var)
