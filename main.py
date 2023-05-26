result = []


def divider(a, b):
    if a < b:
        raise ValueError

    elif a or b != int:
        raise TypeError

    elif b == 0:
        raise ZeroDivisionError

    elif b > 100:
        raise IndexError
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
