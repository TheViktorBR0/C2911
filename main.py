# print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
#
# --------------------------------------------------------------------------------
#
# try:
#     try:
#         print('start')
#         print(error)
#         print('No errors')
#     except SyntaxError:
#         print('Wrong errors')
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print('Next code')
#
# --------------------------------------------------------------------------------
#
# try:
#     print('start')
# except NameError as error:
#     print(error)
# else:
#     print('no problems')
# finally:
#     print('final code')
#
# print('next code')
#
# --------------------------------------------------------------------------------

def checker(a):
    if type(a) != str:
        raise TypeError(f"Sorry, we can't work with {type(a),}, we need class str")
    else:
        return a

var = 10
checker(var)

# --------------------------------------------------------------------------------