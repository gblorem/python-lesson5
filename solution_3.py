# -*- coding: utf-8 -*-

'''
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:

Иванов 23543.12
Петров 13749.32
'''

file = open('./solution_3.txt', 'r')
lines = file.readlines()

middle_salary = 0.0

for line in lines:
	name = line.rsplit()[0]
	surname = line.rsplit()[1]
	salary = line.rsplit()[2]

	if float(salary) < 20000:
		print(' ' + name.ljust(12) + salary)
		middle_salary += float(salary) / len(line.rsplit())

print(' Средний доход сотрудников не достинших 20 тыс оклада = {:.2f}'.format(middle_salary))

file.close()