# li = [1,2,3,4,5]
# li2 = ['a','b','c','d']
# li3 = [1,2,'a', True]
# print(li[2])

# List slicing
amazon_cart = [
	'notebooks',
	'sunglasses',
	'toys',
	'grapes'
]
amazon_cart[0] = 'laptop'
print(amazon_cart[0::2])
new_cart = amazon_cart[:]
# amazon_cart stays the same and new_cart makes a copy of it using [:]
