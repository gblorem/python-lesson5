# -*- coding: utf-8 -*-

'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

nums = input('Добавить целых чисел в файл\n> ').split()

with open('./solution_5.txt', 'a+', encoding='utf-8') as file:
	for num in nums:
		file.write(num + ' ')

with open('./solution_5.txt', 'r', encoding='utf-8') as r_file:
	print('Сумма всех числе файла: ' + str(sum(map(int, r_file.read().split()))))