#!/usr/bin/env python
# -*- coding: utf-8 -*- 

if __name__ == "__main__":
    for example in ["(1+2*(3+4)-100)", "Привет)))", "(cons (fn (car items)) (map fn (cdr items", "))(())(("]:
        parentheses = []  # тут будем хранить открывающие скобки, т.е '('.
        is_balanced = True  # по умолчанию будем считать, что круглые скобки сбалансированы.

        for char in example:  # char - очередной символ введённой пользователем строки.
            if char == '(':
                # Запоминаем, что нашли открывающую скобку.
                parentheses += [char]
            elif char == ')':
                if not parentheses:  # по-другому это можно записать как parentheses == [].
                    # Мы нашли закрывающую скобку для которой не было открывающей.
                    is_balanced = False  # баланс круглых скобок нарушен!
                    break
                else:
                    # Мы нашли закрывающую скобку для которой ранее запомнили открывающую. Всё в порядке, идем дальше.
                    parentheses = parentheses[:-1]

        if is_balanced and not parentheses:
            print("%s -> ПРАВИЛЬНО" % (example))
        else:
            print("%s -> НЕПРАВИЛЬНО" % (example))

# Вывод:
# (1+2*(3+4)-100) -> ПРАВИЛЬНО
# Привет))) -> НЕПРАВИЛЬНО
# (cons (fn (car items)) (map fn (cdr items -> НЕПРАВИЛЬНО
# ))(())(( -> НЕПРАВИЛЬНО
