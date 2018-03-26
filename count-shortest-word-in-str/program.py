from sys import stdin
from re import split
from re import sub


# Функция для определения длины слова:
def get_word_length(word):
    return len(sub(r"\W", "", word))


print("Введите строку -> ")
input_string = stdin.readline().rstrip()

# Разбиваем содержимое на слова, используя пробел в качестве разделителя:
words = split(r'\s', input_string)
print("\nСписок слов:\n{}\n".format(words))

# Подсчитываем длину каждого слова, исключая при этом из слова все символы к нему не относящиеся (запятые и прочее):
words_lengths = list(map(get_word_length, words))
print("Список длин слов:\n{}\n".format(words_lengths))

# Длина самого короткого слова:
min_word_length = min(words_lengths)
print("Длина самого короткого слова = {}\n".format(min_word_length))

# Все слова самой короткой длины:
min_length_words = list(filter(lambda word: get_word_length(word) == min_word_length, words))
print("Список слов самой короткой длины:\n{}\n".format(min_length_words))

# Подсчитываем сколько раз в заданной строке встречается самое короткое слово:
result = {}
for word in min_length_words:
    result[word] = result[word] + 1 if word in result else 1

print("Количество раз, которое встречается самое короткое слово:\n{}\n".format(result))
