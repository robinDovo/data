data = ['a','b','c','d']

count = 0
while count != '-1':

	count = input('請輸入增加單字')
	if count != '-1':
		data.insert(0,count)

print(data)