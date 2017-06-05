#Lab 5
import random

listOfNumbers = [random.randint(-50, 50) for i in range(19)]
print(listOfNumbers)
posOfFirstNegative = -1
i = 0
while (posOfFirstNegative < 0) and (i < len(listOfNumbers)):
	if listOfNumbers[i] < 0:
		posOfFirstNegative = i
	i += 1
if posOfFirstNegative < 0:
	print('Нет отрицательных чисел в списке')
else:
	sum = 0
	i = 0
	while i < posOfFirstNegative:
		sum += listOfNumbers[i]
		i +=1
	print('Сумма всех чисел до первого отрицательного\n\t= {}'.format(sum))
input()
