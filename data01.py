data = ['Apple','Car','Dog','Apple']
n = data.index('Dog')
print(n)

n = data.count('Cat')
print(n)




data = ['apple','Car','Dog','Apple']
while True:
	key = input('請輸入收尋字:')
	if key == '-1':
		break
	if data.count(key) == 0:
		print('找不到')
	else:
		n = data.index(key)
		print('有,在清單中...')