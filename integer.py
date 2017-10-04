num_1 =1
num_2 = 5

print(num_1+num_2)

print( 7%2)
print( 7/2)
print(7//2)
print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 >num_2)

num_3 = '200'
num_4 = '100'
print(num_3+num_4)
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3+num_4)

print(type(num_1))


""" LIST """

courses =['english', 'vinglish', 'tamil', 'Telugu']
print(courses[1]) # to print the second value 

print(courses[-1]) # to print the last value

courses.append('hindi')

print(courses)

courses.insert(2,'tanglish')
print(courses)

courses_2 = ['urdu', 'arabic']

courses.extend(courses_2)
print(courses)


""" Remove """

courses.remove('Telugu')
print("removing telugu ")
print(courses)


""" Reverse """

courses.reverse()
print(courses)

""" pop"""
poped_value = courses.pop()
print('poping last value')
print(courses)
print('the poped value')
print(poped_value)

""" Sort """
courses.sort()
print(courses)

""" Sort in descending  """
print('sort in descending')

courses.sort(reverse=True)

print(courses)

""" This will alter the list below -----sorted function will not alter the list"""

fruits = ['efruit', 'hfruit','apple', 'bannana', 'cucumber', 'dfruit']

sort_fruits= sorted(fruits)

print(sort_fruits)





""" Index of the value """
print(fruits.index('apple'))

""" To find the value is in List"""

print('goava' in courses)
print('apple' in fruits)

marks =[4, 6,8,2,3,5,7]

print(max(marks))
print(min(marks))
print(sum(marks))

# print(marks.union(fruits))


new_fruits = fruits.pop()

print(new_fruits)













