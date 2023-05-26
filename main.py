result = []
def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

def problems(expression):
    try:
        result = data
        return result
    except ValueError as error:
        return f"Syntax, Error {error}"
    except IndexError as error:
        return f"Name Error, {error}"

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)