# Problem Title : Left Rotation
# Level : EASY

# Complete the 'rotLeft' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d

# General Solution Approach Discussion

# We need to left-shift elements of array by one.
# We can store the first element of the array in a temp variable
# and then iterate through rest of the array and left shift
# remaining elements and then update the last element of array by
# the temp variable that has the first element of the array

# SUB-OPTIMAL SOLUTION
# REMARK : RUNS INTO TIME LIMIT EXCEEDED ERROR
def rotLeft(input_array, number_of_rotations):
    # Write your code here
    while number_of_rotations > 0:
        temp = input_array[0]        
        for i in range(len(input_array)-1):
            input_array[i] = input_array[i+1]
        input_array[-1] = temp 
        number_of_rotations -= 1
    return input_array

# Optimal Solution Approach Discussion
# If we look back at the general solution approach, we can see
# and realize that we are shifting elements one by one for each
# left rotation. That means, in essence, the number of rotations
# of the array  means each element has been left shifted that many
# times. Now, we look at the first and final snapshots of the array
# after rotations, we will realize that we can capture the final
# position of each of the elements as a function of the initial
# position, number of rotations * shiftsize of each rotation
# and the length of an array as that essentially ensures that
# everything (all movement of elements) is happening within
# the confines of the array length.

# OPTIMAL SOLUTION
def rotLeft(input_array, number_of_rotations):
    # Write your code here 
    output_array = []
    for i in range(len(input_array)):
        output_array.append(input_array[(i+number_of_rotations)%len(input_array)])
    return output_array