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

basket = [1,2,3,4,5]
basket.append(100)
basket.insert(4, 200)
basket.extend([300])
basket.pop() #removes the last item in the list
basket.pop(0) #removes the specific index
basket.remove(3) #removes specific value
basket.clear() #removes everything in the list
print(basket)