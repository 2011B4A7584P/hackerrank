# Explanation : Iterating through the array and performing left 
# shift of all elements except the last index. The first element
# is stored temporarily for update of the last index.

# Suboptimal solution BRUTE FORCE APPROACH : passes all test cases
# BUT produces TLE
# Space complexity : O(r) where r is the number of rotations
# Time complexity : O(n*r) where n is the given array and r is
#                   the number of rotations


def rotLeft(arr, d_rotations):

    if d_rotations == len(arr):
        return arr
    # Write your code here
    rotation_counter = 0
    
    while rotation_counter < d_rotations:
        
        temp = arr[0]
        
        for index in range(len(arr)):
            if index == len(arr)-1:
                arr[index] = temp
            else:
                arr[index] = arr[index + 1]
        #print(arr)
        rotation_counter += 1
    
    return arr
    
print('Array post specified left rotations : ', rotLeft([3,2,5,1,4],3))	
print('Array post specified left rotations : ', rotLeft([1,2,3,4,5],7))  

# Left rotations on an array
# Space Complexity : O(n)
# Time Complexity : O(n)
def rotLeft(arr, rotations):
    
    if rotations == len(arr):
        return arr
    
    output = []
    
    for i in range(len(arr)):
        output.append(arr[(i+rotations)%len(arr)])
    return output
    	
print('Array post specified left rotations : ', rotLeft([3,2,5,1,4],3))	

# Right rotations on an array
# Space Complexity : O(n)
# Time Complexity : O(n)

def rotRight(arr, rotations):
    
    if rotations == len(arr):
        return arr
    
    output = []
    
    for i in range(len(arr)):
        output.append(arr[(i-rotations)%len(arr)])
    
    return output
	
print('Array post specified right rotations : ', rotRight([3,2,5,1,4],3))