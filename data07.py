fruits = list()

while True:
	name = input('請輸入新增水果名:')
	if name == '':
		break
	fruits.append(name)
print('水果有',fruits)

b = True
while b:
	print('水果有:',fruits)
	name = input('請輸入要刪除的水果名稱:')
	if name == '':
		b = False
	count = fruits.count(name)
	if count >0:
		fruits.remove(name)
	else:
		print('找不到')