# # [11:04 AM] N Murugadoss (Unverified)
# def foo():

# 	name = "geek" # Our local variable
 
# 	def bar():

# 		nonlocal name		 # Reference name in the upper scope

# 		name = 'GeeksForGeeks' # Overwrite this variable

# 		print(name)

# 	# Calling inner function

# 	bar()

# 	# Printing local variable

# 	print(name)
 
# foo()





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