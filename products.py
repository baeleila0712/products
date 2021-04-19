import os #operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
			for line in f:
				if '商品, 價格' in line:
					continue #繼續，跳到下一回
				name, price = line.strip().split(',')
				products.append([name, price])
	return products

#讓使用者輸入名稱/價格 
def user_input(products):   
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		products.append([name, price])
	print(products)
	return products

#印出使用者輸入內容
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案，with用來「close」
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		f.write('商品, 價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
			
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案存不存在
		print('檔案存在')
		products = read_file('products.csv')
	else:
		print('檔案不存在')

	products = read_file('products.csv')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()