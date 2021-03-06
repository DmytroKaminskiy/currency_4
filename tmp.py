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

# def foo():
#
#     print('HELLO')
#     print('HELLO')
#     print('HELLO')

# class A:
#     param = 1

# class A:
#     def foo(self):
#         print('A foo')
#
# class B(A):
#     def foo(self):
#         A.foo(self)
#         print('B foo')
#
# print(B.__mro__)
# a1 = A()
# b1 = B()
# a1.foo()
# b1.foo()

# class A:
#     def __str__(self):
#         return f'object A {id(self)}'
#
# a1 = A()
# a1_str = str(a1)
# print(a1_str)

# # is
# class A:
#     pass
#
#
# class B(A):  # B is A
#     pass
#
# # has
# class Element:
#     def __init__(self, element_type, properties):
#         self.element_type = element_type
#         self.properties = properties
#
#
# class ElementFactory:
#     PROPERTIES = {
#         'camera': {
#             'live': 'True',
#         }
#     }
#
#     # def make(self, element_type, properties={}):
#     def make(self, element_type, properties=None):
#
#         if properties is None:
#             properties = {}
#
#         default_properties = self.__class__.PROPERTIES[element_type]
#         default_properties.update(properties)
#
#         return Element(element_type, default_properties)
#
# factory = ElementFactory()
#
# e1 = factory.make('camera')
# print(type(e1))
# print(e1.element_type)
# print(e1.properties)
# e2 = factory.make('camera')
# print(type(e2))
# print(e2.element_type)
# print(e2.properties)


# e1 = Element('camera', {'live': 'True'})
# e2 = Element('camera', {'live': 'True'})



# class B:
#     def __init__(self):
#         self.a = A()

# def gen():
#     counter = 0
#     while True:
#         yield counter
#         print('GEN')
#         counter += 2
#
# generator = gen()
# print(generator is generator.__iter__())
#
# print(generator.__next__())
# print(generator.__next__())
# print(generator.__next__())

key = 1

def encode(value: str):
    # Dima -> [95, 67, 87, 90] -> [96, 68, 88, 91] -> Ejnb
    return ''.join(map(lambda x: chr(ord(x) + key), value))

def decode(value: str):
    # Ejnb -> [96, 68, 88, 91] -> [95, 67, 87, 90] -> Dima
    return ''.join(map(lambda x: chr(ord(x) - key), value))

'''
1. Показать список всех банков.
2. Создать CRUD операции для модели ContactUs (отправить письмо при создании) Serializer.create
3. Добавить сортировку и фильтры для ContactUs
4. Фильтр по поиску

** к пункту 1 показать все рейты связаные с банком (сорс)
{
"results": [
    {
    "id": 1,
    "name": "privatbank",
    "rates_set": [
      {"id": 1, "sale": 23, "buy": 24...}
    ]
    }
]
}

1. Rate - CRUD - API
2. parse_monobank + parse_vkurse

** Registration


1 multiprocessing
2 deploy
3 docker
4 docker-compose

5 fast api / zoom api
6 Парсер work.ua / regular expressions
7 javascript

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFx9ngchJm6Xquij/7LXHYHE9u6aq/cbNoj/ahrETuF0jD9es0QbC/CizMQh7th2BnTBKcm5E2kQuynEdTew52XLwmYSFRkJ44FWeNra0XJZxjPQHij0IDj39r96pbKgFKvw12DAeoWJMl8hJAPHiPJcEMIXEYvHSs6DcJmqZQIVqOL3uJ/pDUQS+1V6CnhI+jJGNL87yP/HvIb2F9s4OZ6ftuaHUDphauIn3hU5gATvmQ+9mlz5LTazum5dSfRjOzTQ7gILqq7Mee+fPgkvBxsBX/4Z/3gWPGVOM8nlEOILpD4dPospYqAHCyERFkIvJjSVUBnYJ6my/4EzlJKpHr dmytrokaminskiy@dmytrokaminskiy-All-Series
'''

def add(x, y, callback=None):
    if callback is not None:
        callback(x, y)

    return x + y

def get_callback():
    if True:
        return print
    else:
        return lambda x, y: print(x * 2 + y * 2)

r = add(2, 2, callback=get_callback())
r2 = add(2, 2, callback=get_callback())
