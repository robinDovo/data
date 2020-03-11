scores = list()

total = number = 0

while number != -1:
	number = int(input('請輸入學生分數:'))
	if number != -1:
		scores.append(number)
		total += number

avg = total/len(scores)
print('全班人數%d個,總分:%d,平均:%.2f'%(len(scores),total,avg))
