# Fuctions are required, when you need to re use the code several time 
#  One change at the function, it will implement where fun is called 
# Will have  accept set of input and give the output -- print(len("suresh"))

def hellofun():
	pass

print(hellofun())

def hello_fun():
	print('Hello World!')

hello_fun()
hello_fun()

def hello_func():
	return "Hi Da"

hello_func # it  will not give out put , u should use print

print(hello_func())
 

def welcome(greeting, name = 'suresh'):               # even if you to pass the value of the name argu, it will return the default value of suresh --- greeting variable are local with in the function
	return '{}, {}!'.format(greeting, name)
 
print(welcome('Hello'))

print(welcome('Hello', 'Suresh Raju'))

def student_info(args, KWargs):
	print(args)
	print(KWargs)
courses = ['math', 'sci', 'geo', 'civics']
data = { 'name':'suresh', 'age': 23, 'marital_status': 'single'}
# student_info('may', 'june', 'july', name = 'suresh', age = 21, address = 'sembakkam')
student_info(courses,data)
#student_info(*courses, **data)

###########################  #####################
def student_info(*args, **KWargs):
	print(args)
	print(KWargs)
courses = ['math', 'sci', 'geo', 'civics']
data = { 'name':'suresh', 'age': 23, 'marital_status': 'single'}
# student_info('may', 'june', 'july', name = 'suresh', age = 21, address = 'sembakkam')
# student_info(courses,data)
student_info(*courses, **data)
