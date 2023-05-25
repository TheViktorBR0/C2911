def calculate(expression):
    try:
        result = eval(expression)
        return result
    except SyntaxError as error:
        return f"Syntax, Error {error}"
    except NameError as error:
        return f"Name Error, {error}"
    except TypeError as error:
        return f"Type Error, {error}"
    except ZeroDivisionError as error:
        return f"Error, {error}"

while True:
    expression = input("Enter a calculation: ")
    result = calculate(expression)
    print("Result:", result)

    another_calculation = input("Do you want to perform another calculation? (Yes/No): ")
    if another_calculation.lower() == "no":
        break
    elif another_calculation.lower() == "yes":
        calculate()
    else:
        break