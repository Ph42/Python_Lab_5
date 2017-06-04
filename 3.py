#Лаб 3
import random

m, n = [int (i) for i in input('Введите m, n (через пробел)\n').split()]
p = 1
EstChisla = False
if (m != n):
	EstChisla = True
	if m > n:
		m,n = n,m
	for i in range(m, n+1):
		if i % 2 == 0:
			p *= i

if EstChisla:
	print('Произведение квадратов чётных чисел в заданном интервале = {}'.format(p))
else:
	print('Нет целых чисел в интервале')
input()