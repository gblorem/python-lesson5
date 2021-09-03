# -*- coding: utf-8 -*-

'''
2. Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
'''

file = open('./solution_2.txt', 'r')
lines = file.readlines()

line_count = len(lines)
print('\n Файл:         ' + file.name)
print('\n Кол-во строк: ' + str(line_count) + '\n')

i = 0
while i < line_count:
	word_length = len(lines[i].split(' '))
	print(' Строка: ' + str(i + 1) + ' - кол-во слов: ' + str(word_length) + '\n Содержимое: ' + lines[i])
	i += 1
print()

file.close()

# Мало времени, сделал бы еще исключения для цифр