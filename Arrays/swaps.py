# Problem Title : Minimum Swaps 2
# Level : MEDIUM

# RECURSIVE APPROACH : Check if arr has i+1 as value at index i
#                      else perform a swap, return the current
#                      swap count and add it to recursive
#                      swap count of subsequent iterations

# Space complexity : O(1)*total_recursive_calls = O(1)
# Time complexity : O(n)*total_recursive_calls = O(n)

def minimumSwaps(arr):
	
	swaps = 0
	
	if len(arr) in [0,1] or arr == list(range(1,len(arr)+1)):
		return swaps
	
	if len(arr) == 2:
		return 1
		
	else:
		for index, value in enumerate(arr):
			if value == index + 1:
				continue
			else:
				swaps += 1
				arr[index], arr[value-1] = arr[value-1], arr[index]
				
	return 	swaps + minimumSwaps(arr)
	
print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))	
print(minimumSwaps([4, 3, 1, 2]))
print(minimumSwaps([2, 3, 4, 1, 5]))
print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))