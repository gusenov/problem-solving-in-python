# -*- coding: utf-8 -*-

import random

# Напишите класс с именем reverse_iter, который выполняет обратный итератор для списков.
class reverse_iter(list):
    def __init__(self, lst):
        super(reverse_iter, self).__init__()
        self.lst = lst
        self.idx = len(self.lst)

    def next(self):
        if self.idx > 0:
            self.idx -= 1
            return self.lst[self.idx]
        else:
            return None

    def __iter__(self):
        return self


# Пример использования:
# it = reverse_iter([1, 2, 3, 4])
# print(it.next())
# print(it.next())
# print(it.next())
# print(it.next())

# Только для целей этого раздела вы можете использовать случайный пакет, с которым вы столкнулись ранее.
# Запустите генератор с именем roll_pair_of_dice, который возвращает tuple со случайным броском из двух кубов.
def roll_pair_of_dice():
    while True:
        yield (random.randint(1,6), random.randint(1,6))


# Пример использования:
# roll_iter = roll_pair_of_dice()
# print(next(roll_iter))
# print(next(roll_iter))

# Реализуйте функцию range, в форме генератора. Имя функции будет myRange.
# Конечно, сам range или что-то еще не следует использовать, чтобы сделать реализацию тривиальной.
# Также обратите внимание, что вы применяете все варианты range (включая, например, итерацию от высокого к низкому путем отрицательных скачков).
# Вы можете предположить, что вход правильный (целые числа, а скачок не равен нулю).
# Когда дополнительных объектов нет, итератор должен выкинуть ошибку, как обычный оператор, используя команду raise StopIteration()

def myRange(*args):
    if len(args) >= 3:
        a, b, s = args[0], args[1], args[2]
    elif len(args) >= 2:
        a, b, s = args[0], args[1], 1
    elif len(args) >= 1:
        a, b, s = 0, args[0], 1
    else:
        raise TypeError("myRange expected at least 1 arguments, got {0}".format(len(args)))

    if (a < b and s < 0) or (a > b and s > 0):
        return

    i = 0
    el = a + i * s  # i-й элемент
    while el < b:
        yield el
        i += 1
        el = a + i * s

    raise StopIteration()
