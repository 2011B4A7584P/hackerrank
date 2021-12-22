# Brute Force Approach -> passes all test cases but produces TLE
# Passing through the operations (queries) array and performing
# the operation one by one on the original array and returning the 
# max from the resulting final array

# Space complexity : O(n) where n is the input size of the 0-array
# Time complexity : O(n*m) where n is the input size of the 0-array
# m is the size of operations(queries) array
                    
def arrayManipulation(n, queries):
    
    # Write your code here
    array = [0]*n
    
    for i in range(len(queries)):
        for k in range(queries[i][0]-1,queries[i][1]):
            array[k] += queries[i][2]
    
    return max(array)
    
print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))    
print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]])) 
print(arrayManipulation(10, [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]))
print('------XXX-------')

# Space inefficient approach - passes all test cases but numpy
# module is not available for submission, hence 
# benchmarking against all testcases and cannot be ascertained for
# TLE

# Space Complexity - O(n)-for the initial array + 
#                    O(m*n)-for the intermittent arrays inside loop
# Time Complexity - O(n) (for the max decision) + O(n*m) (for the loop computation)                                
import numpy as np

def arrayManipulation(n, queries):
    # Write your code here
    
    array = [0]*n
    
    for i in range(len(queries)):
        
        start_index = queries[i][0]-1
        end_index = queries[i][1]-1
        
        front = [0]*start_index
        rear = [0]*(n-end_index-1)        
        
        operand_array = front + [queries[i][2]]*(end_index - start_index + 1)+ rear
        
        array = np.array(array)
        operand_array = np.array(operand_array)
        array = array + operand_array        
        
    return max(array)
    
print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))    
print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]])) 
print(arrayManipulation(10, [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]))
print('------XXX-------')

# Optimal Approach : Using Prefix Algorithm
# Adding k at index a-1 and subtracting k and index b

# Space complexity : O(n) + O(1) + O(1)
# Time complexity : O(n) (prefix algo upds) + O(m) (prefix sum and maxing out)

def arrayManipulation(n, queries):
    # Write your code here
    array = [0]*n
    
    for i in range(len(queries)):
        array[queries[i][0]-1] += queries[i][2]
        if queries[i][1] < len(array):
            array[queries[i][1]] -= queries[i][2]   
    
    arrSum = 0
    maxSum = 0
    
    for i in array:
        arrSum += i
        maxSum = max(arrSum, maxSum)
        
    return maxSum

#print(arrayManipulation(5, [[1,3,5],[2,4,6],[3,5,1]]))    
print(arrayManipulation(10, [[1,5,3],[4,8,7],[6,9,1]]))    
print(arrayManipulation(5, [[1,2,100],[2,5,100],[3,4,100]])) 
print(arrayManipulation(10, [[2,6,8],[3,5,7],[1,8,1],[5,9,15]]))
print('------XXX-------')
