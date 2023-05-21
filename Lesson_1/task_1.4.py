"""Задание к уроку 1
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
   строкового представления в байтовое и выполнить обратное преобразование
   (используя методы encode и decode)."""

word1 = 'разработка'
word2 = 'администрирование'
word3 = 'protocol'
word4 = 'standard'

word_list = [word1, word2, word3, word4]
word_list_decoded = []
word_list_encoded = []

for word in word_list:
    word_list_encoded.append(word.encode('utf-8'))
print(word_list_encoded)

for words in word_list_encoded:
    word_list_decoded.append(words.decode('utf-8'))
print(word_list_decoded)



