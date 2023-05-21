"""Задание к уроку 1
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
   в последовательность кодов (не используя методы encode и decode) и определить тип,
   содержимое и длину соответствующих переменных.
"""

word1 = b'class'
word2 = b'function'
word3 = b'method'

word_list = [word1, word2, word3]
for word in word_list:
    print(f'"{word}" тип переменной {type(word)}, {len(word)}')
