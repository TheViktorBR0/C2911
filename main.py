result = []


def divider(a, b):
    if type(a) != int:
        raise TypeError

    elif a < b:
        raise ValueError

    elif b > 100:
        raise IndexError

    return a / b


data = {10: 2, 1: 5, "123": 4, 18: [], 0: 15, 8: 4}

print('TypeError, ValueError, IndexError')

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
