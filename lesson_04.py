#1. Проанализировать скорость и сложность одного любого алгоритма, 
#разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
#Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. 
#Результаты анализа сохранить в виде комментариев в файле с кодом.


import time


class MyTester:
	def __init__(self, func, tries):
		self.func = func
		self.tries = tries
		self.res = []
	def test(self, *args):
		for i in range(self.tries):
			start = time.time()
			self.func(*args)
			self.res.append(time.time() - start)
		return sum(self.res) / len(self.res)

def test_func():
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
	return ans


def simple_number_by_index(index):

	s_list = [True for x in range(index * 20)]
	n_index = 1
	num = 2
	sq_num = num ** 2
	while sq_num <= len(s_list):
		if s_list[num]:
			for i in range(sq_num, len(s_list), num):
				s_list[i] = False
		num += 1
		sq_num = num ** 2

	for i in range(2, index * 20):
		if s_list[i]:
			if n_index  == index:
				return i
			n_index += 1

def simple_number_by_index_low(index):
	def is_simple(num):
		for i in range(2, round(num ** 0.5) + 1):
			if num % i == 0:
				return False
		return True

	def next_simple(num):
		num += 1
		while not is_simple(num):
			num += 1
		return num


	n_index = 1
	num = 2
	
	while n_index != index:
		num = next_simple(num)
		n_index += 1

	return num


a = int(input('Enter number or tries: '))
#res = MyTester(test_func, a)
res_low = MyTester(simple_number_by_index_low, a)
res = MyTester(simple_number_by_index, a)


print('Average time: {}'.format(res_low.test(100000))) #сложность этого алгоритма можно оценить как O(n^2)
print('Average time: {}'.format(res.test(100000))) #сложность этого - O(n * log(n))