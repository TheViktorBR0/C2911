result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)
    try:
        result = eval()
        return result
    except SyntaxError as error:
        return f"Syntax, Error {error}"

print(result)

def problems(data):
    try:
        result = eval(data)
        return result
    except SyntaxError as error:
        return f"Syntax, Error {error}"
    except NameError as error:
        return f"Name Error, {error}"
    except TypeError as error:
        return f"Type Error, {error}"
    except ZeroDivisionError as error:
        return f"Error, {error}"