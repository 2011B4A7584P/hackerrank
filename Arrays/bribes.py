# Problem Title : New Year Chaos
# Level : MEDIUM

# Complete the 'minimumBribes' function below
# The function accepts INTEGER_ARRAY q as parameter


# SUBOPTIMAL SOLUTION
# BRUTE FORCE APPROACH : gives correct output
# but fails on few test cases due to time limit 
# exceeded error

# Checking for no bribes, more than 2 bribes
# And then checking for cases of 1 and 2 bribes at each index

# Space complexity : O(1)
# Time complexity : O(n*n)

def minimumBribes(queue):
    
    bribes = 0
    
    if len(queue) in [0,1] or queue == list(range(1,len(queue)+1)):
        return bribes
        
    for current, value in enumerate(queue):
        if value - (current + 1) > 2:
            print('Too chaotic')
            return
        else:
            j = 0
            while j < current:
                if queue[j] > value:
                    bribes += 1
                j += 1    
    
    print(bribes)
    
minimumBribes([2, 1, 5, 3, 4])
minimumBribes([2, 5, 1, 3, 4])
minimumBribes([4, 1, 2, 3])
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])

print('------------------------------')

# OPTIMAL SOLUTION : ELEGANT, INTUITIVE
# Approach 1 : There are only two cases broadly :
# Case 1 : Value i+1 is at index i, which means there is no bribe for this position
# Case 2 :
#          Subcase 1 : Value at index i is more than index by 3 which means there have been too many bribes
#          Subcase 2 : Value at index i-1 is i+1, and therefore a swap would put the array in correction for index i
#          Subcase 3 : Value at index i-2 is i+1, and therefore two swaps would put the array in correction for index i
# Space complexity : O(1)
# Time complexity : O(n) where n is the length of the queue

def minimumBribes(queue):
    bribes = 0
    if len(queue) in [0,1] or queue == list(range(1,len(queue)+1)):
        return bribes
	    
    else:
        for index, value in enumerate(queue):
            if value - (index + 1) > 2:
                return 'Too chaotic'
        
        i = len(queue) - 1
        while i>=0:
            if i-1 >=0 and queue[i] != i + 1 and queue[i-1] == i + 1:
                bribes += 1
                queue[i-1], queue[i] = queue[i], queue[i-1]
            elif i-2>=0 and queue[i] != i + 1 and queue[i-2] == i + 1:
                bribes += 2
                queue[i-2], queue[i-1] = queue[i-1], queue[i-2]
                queue[i-1], queue[i] = queue[i], queue[i-1]
                
            i -= 1
        return bribes
	
print(minimumBribes([2, 1, 5, 3, 4]))
print(minimumBribes([2, 5, 1, 3, 4]))
print(minimumBribes([4, 1, 2, 3]))
print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
print('------------------------------')

# SUBOPTIMAL SOLUTION :NOT ELEGANT, NOT INTUITIVE BUT PASSES ALL TEST CASES
# Space Complexity : O(1)
# Time Complexity : O(n*k) where k <= 2

def minbribes(queue):
	
    bribes = 0
    for current_position, value in enumerate(queue):
        if value - 1 - current_position > 2:
            print('Too chaotic')
            return
        for k in range(max(0, value-2), current_position):
            if queue[k] > value:
                bribes += 1
                
    print(bribes)
    
minbribes([2,1,5,3,4])
minbribes([2,5,1,3,4])
minbribes([4,1,2,3])
minbribes([1,2,5,3,7,8,6,4])
print('------------------------------')