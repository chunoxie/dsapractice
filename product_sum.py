# runs in O(n) time | O(d) space, where n is a count of all the elements 
# in the array including all the elements in the sub-arrays while d is the 
# depth of the sub-array

def product_sum(array, multiplier = 1):
	sum = 0

	for element in array:
		if type(element) is list:
			sum += product_sum(element, multiplier + 1)
		else:
			sum += element
	return sum * multiplier

print(product_sum([1, 2, 3, 4, 5, [1, 2, 3, 4, 5]]))