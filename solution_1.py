# -*- coding: utf-8 -*-

'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''


# Simple
print('Для завершения оставьте строку пустой.\n')
while True:
	new_line = input('Введите текст строки:\n> ')
	if not new_line:
		print('\nЦикл был завершен.')
		break
	else:
		file = open('./solution_1.txt', 'a+', encoding='utf-8')
		file.write(str(new_line) + '\n')
		print('\nДанные были записаны')
		file.close()

# Junior