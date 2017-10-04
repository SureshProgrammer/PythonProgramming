nums =[1,2,3,4]
for num in nums:
	if num ==3:
		print('found the 3 lets exit of the loop by break')
		break
	print(num)


# # use continue to ignore the value 3 alonr 

nums =[1,2,3,4]
for num in nums:
	if num ==3:
		print('found the 3 lets ignore it and continue the loop')
		continue
	print(num)

# nested for loop

for num in nums:
	for letter in 'abcd':
		print(num,letter)
	print('end of ' + str(num) + ' iteration')

# For loop using range 


for q in range(1, 11):
	print(q)

	############################### While ############
g =1

while g < 10:
	print(g)
	# g = g + 1
	g+= 1

while g< 15:
	print('new while')
	if g==13:
		break
	print(g)
	g+=1

	############
p=0
# while True:
# 	print(p)
# 	p+=1
