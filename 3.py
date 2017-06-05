import random

#listOfNumbers = [random.randint(-50, 50) for i in range(15)]
listOfNumbers = [i for i in input('Введите через пробел элементы последовательности').split()]


'''
print('posOfFirstNegative = ', posOfFirstNegative)
print('posOfFirstZero = ', posOfFirstZero)

if (posOfFirstNegative < 0) or (posOfFirstZero < 0):
	print('В списке отсутствует одно или оба из искомых чисел границы интервала: отрицательное и равное нулю')
else:
	sum = 0
	i = 0
	a, b = posOfFirstNegative, posOfFirstZero # Границы интервала
	if a > b:
		a, b = b, a
	slice1 = []
	for i in range(a+1,b):
		sum += listOfNumbers[i]
		slice1.append(listOfNumbers[i])
		i +=1
	print('Искомые элементы = listOfNumbers[{:4.2f}:{}] = {}'.format(a+1,b,slice1))
	print('Сумма всех чисел между первым отрицательным и первым нулевым элементами\n\t= {}'.format(sum))
input()
'''