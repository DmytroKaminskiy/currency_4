# t = (1, 2, [3, 4])
# t[-1].append(5)
# t[-1] = [3, 4, 5]
#
# print(t)

# l1 = [1, 2]
# l2 = l1
#
# l1.append(3)
# print(l2)

# l1 = [1, 2, 3]
# l2 = [1, 2, [3, 4]]
# l1 = [1, 2, 3]
# s1 = '123'
# d1 = {1: 1, 2: 2}

# print(dir(d1))
# for item in s1:
#     print(item)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __add__(self, other):
#         # WRONG return Cat()
#         return self.__class__(self.name + other.name, 0)
#
#     def __iter__(self):
#         return self.name.__iter__()
#
# c1 = Cat('Tom', 5)
# for char in c1:
#     print(char)
# c2 = Cat('Alisa', 3)
# c3 = c1 + c2 + c1 + c2 + c1
# c3 = c1.__add__(c2.__add__(c1.__add__((c2.__add__(c1)))))
# print(c3.name)
# print(c3.age)
# print(type(c3))
# print(dir(c3))
# print(dir(c1))

# l1 = [1, 2, 3]
# iter_l1 = l1.__iter__()
# print(iter_l1.__next__())
# print(iter_l1.__next__())
# print(iter_l1.__next__())
# print(iter_l1.__next__())

# from collections import defaultdict, Counter

# d = {}
# def foo():
#     return ['HELLO']

# d = defaultdict(foo)
# {0: [], 1: []}

# key1 = 1
# d[key1].append('TEST')
# print(d)
# if key1 in d:
#     d[key1].append('TEST')
# else:
#     d[key1] = ['TEST']

# d = [1, 1, 1, 3, 2, 2]
# print(Counter(d).most_common(1))

# class RateForm:
#     pass
#
# form = RateForm()

'''
1. ContactUs - форма создания объекта
2. Bank - create & update & delete

'''