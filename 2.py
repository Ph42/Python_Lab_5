#Lab 5
import random

listOfNumbers = [random.randint(-50, 50) for i in range(15)]
#listOfNumbers = [1, 5, 0, 9, 1, 1, 1, 1, 15, -1, 21, 14, 5, 7]  -  для тестирования
print(listOfNumbers)
posOfFirstNegative = -1
posOfFirstZero = -1
i = 0
while ((posOfFirstNegative < 0) or (posOfFirstZero < 0)) and (i < len(listOfNumbers)):
	if (listOfNumbers[i] < 0) and (posOfFirstNegative < 0):
		posOfFirstNegative = i
	if (listOfNumbers[i] == 0) and (posOfFirstZero < 0):
		posOfFirstZero = i	
	i += 1
i = 0

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
	print('Искомые элементы = listOfNumbers[{}:{}] = {}'.format(a+1,b,slice1))
	print('Сумма всех чисел между первым отрицательным и первым нулевым элементами\n\t= {}'.format(sum))
input()
