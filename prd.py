import os #operating system
products = []
if os.path.isfile('products.csv'):
	print('file found') 
	with open('products.csv','r') as f:
		for line in f:
			if 'product,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('404 not found')

while True:
	name = input('plz enter product name: ')
	if name == "q":
		break
	price = input('enter price: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(product)
for p in products:
	print(p[0], 'price is', p[1])

with open('products.csv', 'w') as f:
	f.write('product:,price:\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')