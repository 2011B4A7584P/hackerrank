# Brute force method : Iterating through the array and finding
# each hourglass and it's sum, storing all such hourglassSums
# and then maxing out

# Space complexity : O(n*n)
# Time complexity : O(n*n)

def hourglassSum(arr):
    
    hourglass_sums = []
    
    n_rows = len(arr)
    n_cols = len(arr[0])
    
    for i in range(n_rows - 2):
        for j in range(n_rows - 2):
        
            hourglass_sums.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] +\
                                  arr[i+1][j+1] +\
                                  arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    
    return max(hourglass_sums)

# Space efficient solution : Iterating through the array and finding
# each hourglass and it's sum, comparing with previous hourglassSum
# starting with the first hourglassSum and updating the max

# Space complexity : O(1)
# Time complexity : O(n*n)    
def hourglassSum(arr):

	# hourglassSums = []
	
	max_sum = arr[0][0] + arr[0][1] + arr[0][2] +\
				arr[1][1] + \
				arr[2][0] + arr[2][1] + arr[2][2]
	
	for i in range(len(arr)-2):
		for j in range(len(arr)-2):
			
			hourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] +\
						   arr[i+1][j+1] + \
						   arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
					
			# hourglassSums.append(hourglassSum)
			
			if hourglassSum > max_sum:
				max_sum = hourglassSum
				
	
	return max_sum #max(hourglassSums)