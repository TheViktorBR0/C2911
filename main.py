# --------------------------------------------------------------------------------
#
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
#
#
# def checker(a):
#     if type(a) != str:
#         raise TypeError(f"Sorry, we can't work with {type(a),}, we need class str")
#     else:
#         return a
#
#
# var = 10
# checker(var)
#
# --------------------------------------------------------------------------------
#
#
# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house can't built"
#
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return 'enough materials'
#     else:
#         raise BuildingError(amount_of_material)
#
#
# materials = 300.0000000000001
# print(check_material(materials, 300))
#
# --------------------------------------------------------------------------------
#
# import warnings
#
# warnings.simplefilter('ignore', SyntaxWarning)
# warnings.simplefilter('error', ImportWarning)
#
# warnings.warn('Warning, no code here', SyntaxWarning)
# try:
#     warnings.warn('Warning, module not imported', ImportWarning)
# except:
#     print('warning processed')
#
# --------------------------------------------------------------------------------
