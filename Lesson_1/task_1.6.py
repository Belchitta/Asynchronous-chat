"""Задание 1:
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect
# Записываем необходимые данные и создаём файл
txt_lines = ['сетевое программирование\n',
             'сокет\n',
             'декоратор']

with open('test_file.txt', 'w', encoding='cp866') as f:
    f.writelines(txt_lines)

# уточним кодировку файла:
with open('test_file.txt', 'rb') as f:
    data = f.read()
print(detect(data))
en_coding = detect(data)['encoding']
print(en_coding)

# открываем файл в нужной кодировке
with open('test_file.txt', 'r', encoding=en_coding) as f:
    data = f.read()
print(data)
