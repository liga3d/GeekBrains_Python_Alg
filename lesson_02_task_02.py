# Написать функцию для записи значений солваря в файл
import json

INITIAL_DATA = dict(Name = [3, 1, 2, 3, 4], Surname = [3, 4, 5, 6, 7, 8], Fathername = [3, 4, 5, 6, 7, 8])

def save(filename, data):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write(data)

def load(filename):
	with open(filename, 'r', encoding='utf-8') as f:
		data = f.read()
	return data

save('data.db', json.dumps(INITIAL_DATA))
data = json.loads(load('data.db'))
print(data, type(data))
