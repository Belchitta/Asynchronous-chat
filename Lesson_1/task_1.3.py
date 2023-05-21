"""Задание к уроку 1
3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе."""


# Поскольку слова "класс","функция" содержат не только символы ASCII, их нельзя закодировать в байты,
# проверяем предположение:
word1 = 'attribute'
word2 = 'класс'
word3 = 'функция'
word4 = 'type'

word_list = [word1, word2, word3, word4]
for word in word_list:
    try:
        print(f'"{word}" в закодированном виде: {bytes(word, "ascii")}')
    except UnicodeEncodeError:
        print(f'"{word}" содержит не только символы ASCII')
