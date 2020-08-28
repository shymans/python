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
#print(amazon_cart[0::2])
new_cart = amazon_cart[:]
# amazon_cart stays the same and new_cart makes a copy of it using [:]

basket = [1,2,3,4,5]
basket.append(100)
basket.insert(4, 200)
basket.extend([300])
basket.pop() #removes the last item in the list
basket.pop(0) #removes the specific index
basket.remove(3) #removes specific value
# basket.clear() #removes everything in the list
# print(basket)

bag = ['a','b','c','d','e','d']
#print(bag.index('d', 0, 4))
#print('d' in bag)
bag.count('d')
bag.sort() #organizes actual list
sorted(bag) #creates new copy of the bag and sorts it
bag.reverse()

#print(list(range(100)))
words = ' '.join(['hi', 'my', 'name', 'is', 'Jojo'])
print(words)


#list unpacking
a,b,c *other, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)

