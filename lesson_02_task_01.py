# задание 1
# Есть 2 игрока и 25 монет. Каждый может брать от 1 до 3 монет за ход. 
# Проигрывает тот, кто забрал последнюю.

MAX_COINS_COUNT = 25
MAX_SELECT = 3
MIN_SELECT = 1

class Coins:
	def __init__(self, coins_count):
		self.coins_count = coins_count
	def get_coins(self, quantity):
		self.coins_count -= quantity
		print('Убрано монет: {}'.format(quantity))
	def __str__(self):
		self.str = (chr(1) + ' ') * self.coins_count + '\n'
		self.str += 'Осталось {}\n'.format(self.coins_count)
		return self.str

class Player:
	def __init__(self, name):
		self.name = name
	def turn(self):
		select = 0
		while select not in range(MIN_SELECT, MAX_SELECT + 1):
			try:
				select = int(input('Ваш ход, сколько монет Вы хотите забрать? (от {} до {}):'.format(MIN_SELECT, MAX_SELECT)))
			except ValueError:
				continue
		return select

class AI:
	def __init__(self, name):
		self.name = name
		self.last_coins_count = MAX_COINS_COUNT
		self.pack = MIN_SELECT + MAX_SELECT
	def turn(self, coins):
		print('Ход компьютера:\n')
		select = self.pack + coins.coins_count - self.last_coins_count
		self.last_coins_count -= self.pack
		return select

a = Coins(MAX_COINS_COUNT)
p_name = input('Добро пожаловать в игру!\nВведите Ваше имя:')
player = Player(p_name)
comp = AI('Суперкомпьютер')

while True:
	print(a)
	a.get_coins(player.turn())
	print(a)
	if a.coins_count <= 0:
		print('К сожалению, {}, Вы проиграли :)\nПобедил {}'.format(player.name, comp.name))
		raise SystemExit
	a.get_coins(comp.turn(a))
	if a.coins_count <= 0:
		print('Вы выиграли, хотя эта строчка никогда не будет напечатана:)')
		raise SystemExit
