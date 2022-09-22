# *args: Unlimited Arguments
# @returns a tuple
# def add(*args):
#     return sum(args)
# print(add(1, 2, 3, 4, 5, 6))
#
#
# **kwargs: Many Keyword Arguments (Unlimited Keyword Arguments)
# @returns a dictionary
# def calculate(n, **kwargs):
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
#
# calculate(5, add=4, multiply=9)
# for key, value in dict.items():
#    print(key)
#    print(value)
#
# users = [
#     {
#         'id': '_user1',
#         'name': 'Nazir',
#         'age': 21
#     },
#     {
#         'id': '_user2',
#         'name': 'Egemen',
#         'age': 46
#     }
# ]
# for dicts in users:
#     for key, value in dicts.items():
#         print(f'{key} : {value}')
