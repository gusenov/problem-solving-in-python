def check(s):
    parentheses = []  # тут будем хранить открывающие скобки, т.е '('.
    is_balanced = True  # по умолчанию будем считать, что круглые скобки сбалансированы.

    for char in s:  # char - очередной символ введённой пользователем строки.
        if char == '(':
            # Запоминаем, что нашли открывающую скобку.
            parentheses.append(char)
        elif char == ')':
            if not parentheses:  # по-другому это можно записать как parentheses == [].
                # Мы нашли закрывающую скобку для которой не было открывающей.
                is_balanced = False  # баланс круглых скобок нарушен!
                break
            else:
                # Мы нашли закрывающую скобку для которой ранее запомнили открывающую. Всё в порядке, идем дальше.
                parentheses.pop()

    if is_balanced and not parentheses:
        return True
    else:
        return False


if __name__ == "__main__":
    for example in ["(1+2*(3+4)-100)", "Привет)))", "(cons (fn (car items)) (map fn (cdr items", "))(())(("]:
        if check(example):
            print("{0} 🡺 ПРАВИЛЬНО".format(example))
        else:
            print("{0} 🡺 НЕПРАВИЛЬНО".format(example))

# Вывод:
# (1+2*(3+4)-100) 🡺 ПРАВИЛЬНО
# Привет))) 🡺 НЕПРАВИЛЬНО
# (cons (fn (car items)) (map fn (cdr items 🡺 НЕПРАВИЛЬНО
# ))(())(( 🡺 НЕПРАВИЛЬНО
