#Lab 5
import random

#listOfNumbers = [random.randint(-50, 50) for i in range(15)]
listOfNumbers = [int(i) for i in input('Введите через пробел элементы последовательности:\n\t').split()]
# Образуют ли они арифметическую проггрессию. Если да то вывести разность прогрессии
isArithmeticProgression = False
if len(listOfNumbers) > 1:
	d = listOfNumbers[1] - listOfNumbers[0]	
	i = 2
	isArithmeticProgression = True
	while (i < len(listOfNumbers)) and isArithmeticProgression:
		if listOfNumbers[i] - listOfNumbers[i-1] != d:
			isArithmeticProgression = False
		i += 1
if isArithmeticProgression:
	print('Последовательность является арифметической прогрессией. Разность прогрессии d = {}'.format(d))
else:
	print('Числа последовательности не образуют арифметической прогрессии')
input()
