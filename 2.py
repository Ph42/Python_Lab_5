#Лаб 4 - Строки
s = input('Введите строку, для того чтобы разрядить её пробелами:\n\t')
i = 0

while i < len(s):
	if i+1 < len(s):
		if (s[i] != ' ') and (s[i+1] != ' '):
			s = s[:i+1] + ' ' + s[i+1:]
	i += 1
print(s)
input()