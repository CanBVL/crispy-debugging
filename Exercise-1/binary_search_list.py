#!/usr/bin/env python3

def binary_search(list, key):
	list.sort() # Binary search starts with a sorted list
	left = 0 # The first value of the list
	right = len(list) - 1 # The last value of the list
	while left <= right:
		middle = (left + right) // 2
		if list[middle] == key:
			return middle
		if list[middle] > key:
			print("Checking the left side")
			right = middle - 1
		if list[middle] < key:
			print("Checking the right side")
			left = middle + 1
	return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
