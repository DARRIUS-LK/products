product = []
while True:
	name = input('plz enter product name: ')
	if name == "q":
		break
	price = input('enter price: ')
	p = []
	p.append(name)
	p.append(price)
	product.append(p)
print(product)