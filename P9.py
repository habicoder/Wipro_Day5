def foo():
	age = 45 # Our local variable
 
	def bar():
		nonlocal age		 # Reference name in the upper scope
		age = age+1  # Overwrite this variable
		print(age)
	# Calling inner function
	bar()
	# Printing local variable
	print(age)
 
foo()