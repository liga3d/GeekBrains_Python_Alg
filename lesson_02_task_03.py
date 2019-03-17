# Написать класс, который занимается выпечкой. т.е. к него есть методы для:
# 1) добавления количества ингредиентов на склад
# 2) выпечка с указанием рецепта
# 3) просмотр рецептов
# Внутри него зашиты рецепты и в случае если нехватает продуктов, то он говорит каких и сколько ему не хватает

# stock db, recipes db
# ingredients: bread, flour, eggs, oil, tomato, bazil, cheese, peper, pepperoni, ham


class Baker:
	def __init__(self, name):
		self.name = name
		self.stock = dict(
			bread = 10, 
			flour = 10, 
			eggs = 10, 
			oil = 10, 
			tomato = 10, 
			bazil = 10, 
			cheese = 10, 
			peper = 10, 
			pepperoni = 10, 
			ham = 10
			)
		self.recipes = dict(
			pizza = dict(flour = 3, eggs = 1, bazil = 2, oil = 1, tomato = 3, cheese = 2, pepperoni = 2, peper = 1),
			sandwich = dict(bread = 2, eggs = 1, ham = 2, cheese = 2, tomato = 1),
			scrambled_eggs = dict(oil = 1, eggs = 3, tomato = 2, bazil = 1, cheese = 2, ham = 1)
			)

	def bake(self, dish):
		def in_stock(dish):
			for item in self.recipes[dish].keys():
					if self.stock[item] < self.recipes[dish][item]:
						return False
			return True
		if dish in self.recipes.keys():
			if in_stock(dish):
				for item in self.recipes[dish].keys():
					self.stock[item] -= self.recipes[dish][item]
				res_string = 'Ваше блюдо "{}"! Приятного аппетита!'.format(dish)
			else:
				shortage = {}
				for item in self.recipes[dish].keys():
					if self.stock[item] < self.recipes[dish][item]:
						shortage[item] = self.recipes[dish][item] - self.stock[item]
				res_string = 'К сожалению, у нас нехватило следующих ингредиентов: \n'
				for item in shortage.keys():
					res_string += item + ' - ' + str(shortage[item]) + '\n'
		else:
			res_string = 'У меня нет рецепта, чтобы приготовить {}'.format(dish)
		return res_string

	def show_stock(self):
		stock = 'Склад:\n'
		for item in self.stock.keys():
			stock += item + ' - ' + str(self.stock[item]) + '\n'
		return stock

	def fill_stock(self):
		for item in self.stock.keys():
			self.stock[item] += 10

	def show_recipes(self):
		res = 'Рецепты:\n'
		for item in self.recipes.keys():
			res += item + ':\n'
			for ing in self.recipes[item].keys():
				res += '\t' + ing + ' - ' + str(self.recipes[item][ing]) + '\n'
		return res

	def __str__(self):
		self.str = 'Программа кулинар {}!\nЯ могу приготовить:\n'.format(self.name)
		for item in self.recipes.keys():
			self.str += item + '\n'
		return self.str
	
a = Baker('LuckyBackery')

while True:
	print(a)
	s = input('Что для Вас приготовить?\n(q - выход, f - пополнить запасы, s - показать запасы, r - рецепты): ')
	if s == 'q':
		raise SystemExit
	elif s == 'f':
		a.fill_stock()
		print(a.show_stock())
	elif s == 's':
		print(a.show_stock())
	elif s == 'r':
		print(a.show_recipes())
	else:
		print(a.bake(s))