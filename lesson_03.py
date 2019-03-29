import random

#1. В диапазоне натуральных чисел от 2 до 1000000 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def is_div(div, num):
	if div > num:
		return False
	else:
		return num % div == 0

ans = {}

for div in range(2, 10):
	ans[div] = 0
	for num in range(2, 1000001):
		ans[div] += is_div(div, num)

print(ans)

#2. Во втором массиве сохранить индексы четных элементов первого массива. 
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
#то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
#т.к. именно в этих позициях первого массива стоят четные числа.

a = [random.randrange(1, 100) for i in range(50)]

ans = []

for i in range(0, len(a)):
	if a[i] % 2 == 0:
		ans.append(i)

print(a)
print(ans)

#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

a = [random.randrange(1, 100) for i in range(50)]

print(a)

max, min = a.index(max(a)), a.index(min(a))

print('max = {}, index = {}\nmin = {}, index = {}'.format(a[max], max, a[min], min))

a[max], a[min] = a[min], a[max]

print(a)

#4. Определить, какое число в массиве встречается чаще всего.

a = [random.randrange(1, 100) for i in range(500)]

print(a)

ans = {}

for i in a:
	if i not in ans:
		ans[i] = 1
	else:
		ans[i] += 1

max = max(ans.values())

for i in ans.keys():
	if ans[i] == max:
		max_index = i

print('Nuber - {}, count - {}'.format(max_index, max))

#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

a = [random.randrange(0, 101) - 50 for i in range(50)]
b = list(filter(lambda x: x < 0, a))

print(a)
print(max(b))

#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
#Сами минимальный и максимальный элементы в сумму не включать.

a = [random.randrange(1, 100) for i in range(20)]

max, min = a.index(max(a)), a.index(min(a))
if min > max:
	max, min = min, max

print(a)
print(a[min + 1: max])
print(sum(a[min + 1: max]))

#7. В одномерном массиве целых чисел определить два наименьших элемента. 
#Они могут быть как равны между собой (оба являться минимальными), так и различаться.

a = [random.randrange(1, 100) for i in range(20)]

print(sorted(a)[:2])

#8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
#Программа должна вычислять сумму введенных элементов каждой строки 
#и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

ans = []

for i in range(4):
	s = input('enter {} string of matrix, divide by space:'.format(i + 1))
	str_num = [int(num) for num in s.split()]
	str_num.append(sum(str_num))
	ans.append(str_num)

for string in ans:
	[print(data, end=' ') for data in string]
	print('\n')

#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matr = [[random.randint(1, 100) for i in range(10)] for j in range(10)]

for string in matr:
	print(*string, sep=' ')

ans = []

for j in range(len(matr[0])):
	ans.append(min([matr[i][j] for i in range(len(matr))]))

print(ans)
print(max(ans))