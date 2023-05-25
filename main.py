# ----------------------------------------------------------------------------------
#
# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
#
# count = Counter(5)
# for elem in count:
#     print(elem)
#
# ----------------------------------------------------------------------------------
#
# def raise_to_the_degrees(number, max_degree):
#     i = 0
#     for _ in range(max_degree):
#         yield number ** i
#         i += 1
#
#
# res = raise_to_the_degrees(10, 100)
# print(res)
# for _ in res:
#     print(len(str(_)))
#     print(_)
#
# ----------------------------------------------------------------------------------
#
# class Helper:
#     def __init__(self, work):
#         self.work = work
#
#     def __call__(self, work):
#         return f"I will help you with your {self.work}. Afterward I will help you with {work}"
#
#
# helper = Helper('Homework')
# print(helper('Cleaning'))
#
# ----------------------------------------------------------------------------------
#
# def helper(work):
#     work_in_memory = work
#
#     def helper(work):
#         return f"I will help you with your {work_in_memory}. Afterward I will help you with {work}"
#
#     return helper
#
#
# helper = helper('Homework')
# print(helper("cleaning"))
# print(helper("driving"))
#
# ----------------------------------------------------------------------------------

# def checker(function, *args, **kwargs):
#     try:
#         result = function(*args, **kwargs)
#     except Exception as exc:
#         print(f"We have a problems {exc}")
#     else:
#         print(f"No problems. Result - {result}")
#
#
# def calculate(expression):
#     return eval(expression)
#
#
# checker(calculate, '10+10')

# ----------------------------------------------------------------------------------

def checker(*exc_types):
    def checker(function):
        def checker(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except (exc_types) as exc:
                print(f"We have a problems {exc}")
            else:
                print(f"No problems. Result - {result}")

        return checker

    return checker

@checker(NameError, TypeError, SyntaxError, ZeroDivisionError)
def calculate(expression):
    return eval(expression)

calculate(input('Enter calculation: '))

# ----------------------------------------------------------------------------------
