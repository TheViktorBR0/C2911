#print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    print('start')
    print(10/0)
    print('No errors')
# except NameError:
#     print('We have a Name Error')
# except ZeroDivisionError:
#     print('We have a Zero Division Error')
except (NameError, ZeroDivisionError) as error:
    print(error)

print('Next code')