# ----------------------------------------------------------------------------------
#
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
# res = raise_to_the_degrees(10, 100)
# print(res)
# for _ in res:
#     print(len(str(_)))
#     print(_)
#
# ----------------------------------------------------------------------------------

class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help you with your {self.work}. Afterwards i will help you with {work}"

helper = Helper('Homework')
print(helper('Cleaning'))

# ----------------------------------------------------------------------------------