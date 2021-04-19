products = []

with open('products.csv', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		if '商品, 價格' in line:
			continue #繼續，跳到下一回
		name, price = line.strip().split(',')
		products.append([name, price])
		#print(name, '的價格是', price, '元')
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)

#印出使用者輸入內容
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案，with用來「close」
with open('products.csv', 'w', encoding='utf-8-sig') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')