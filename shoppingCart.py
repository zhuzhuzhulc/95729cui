class cart():
	def __init__(self):
		self.items = {}
	'''
	add item to shopping cart 
	'''
	def addToCart(self,item):
		if item.itemName in self.items:
			new_quantity = item.getQuantity()
			old_quantity = self.items[item.itemName].getQuantity()
			self.items[item.itemName].setQuantity(new_quantity + old_quantity)
		else: 
			name = item.itemName
			self.items[name] = item
		return 
	'''
	remove item from shopping cart, item is a string 
	'''
	def removeItem(self,item):
		if item not in self.items:
			print item + " not in shopping cart"
			return 
		self.items.pop(item)
		return 

	'''
	Print every item + quantity in the shopping cart. 
	'''
	def toString(self):
		lst = []
		for (k,item) in self.items.iteritems():
			lst.append((item.name,item.getQuantity()))
		print (lst)
		return 

	'''
	list everything in the shopping cart 
	'''
	def printCart(self):
		for (k,item) in self.items.iteritems():
			name = k
			quantity = item.getQuantity()
			price = item.getPrice()
			totalP = quantity * price 
			print name + " " + quantity + " " + str(totalP)
		return 
	def getTotal(self):
		total = 0
		for (k,item) in self.items.iteritems():
			total += item.getQuantity() * item.getPrice()
			print '--------------------------------------'
			print 'total amount ' + str(total)
		return 

