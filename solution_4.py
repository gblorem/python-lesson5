# -*- coding: utf-8 -*-

'''
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

ru_num_list = {
	0: 'ноль',
	1: 'один',
	2: 'два',
	3: 'три',
	4: 'четыре',
	5: 'пять',
}

with open('./solution_4.txt', 'r', encoding='utf-8') as file:
	for line in file:
		for i in ru_num_list:
			if str(i) in str(line):
				print(f'{ru_num_list[i]} - {i}')
				new_data = str(ru_num_list[i]) + ' — ' + str(i)
				new_file = open('./solution_4_new_file.txt', 'a', encoding='utf-8')
				new_file.write(str(new_data) + '\n')

new_file.close()
file.close()