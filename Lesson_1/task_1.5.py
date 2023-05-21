"""Задание 1
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
"""
import subprocess
import chardet
args = ['ping', 'yandex.ru']
args_ = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
subproc_ping_ = subprocess.Popen(args_, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    data = chardet.detect(line)
    print(data)
    line = line.decode(data['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

for lines in subproc_ping_.stdout:
    response = chardet.detect(lines)
    print(response)
    lines = lines.decode(response['encoding']).encode('utf-8')
    print(lines.decode('utf-8'))

