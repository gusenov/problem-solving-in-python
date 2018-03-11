from functools import reduce
from re import sub
from re import split

with open("input.txt") as f:
    contents = f.read()  # считываем содержимое входного файла.
    print("Содержимое входного файла:\n{}\n".format(contents))

    # Разбиваем содержимое на слова, используя пробел или перевод строки в качестве разделителя:
    words = split(r'\s|\n', contents)
    print("Список слов:\n{}\n".format(words))

    # Подсчитываем длину каждого слова, исключая при этом из слова все символы к нему не относящиеся (запятые и прочее):
    words_lengths = list(map(lambda word: len(sub(r"\W", "", word)), words))
    print("Список длин слов:\n{}\n".format(words_lengths))

    # Суммируем все слова длина которых не более четырех букв:
    result = reduce(lambda result_sum, word_length: result_sum + (1 if word_length <= 4 else 0), [0] + words_lengths)
    print("Количество слов, состоящих не более чем из четырех букв = {}".format(result))  # вывод результата на экран.
