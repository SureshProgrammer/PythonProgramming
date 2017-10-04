print('to confirm that this module is imported')

def find_index(listname, element):
	for index, values in enumerate(listname):
		if values == element:
			return index
	return -1

stringy = 'python learning'