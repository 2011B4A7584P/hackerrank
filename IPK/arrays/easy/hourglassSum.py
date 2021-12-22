# Problem Title : 2D Array - DS
# Level : EASY


# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def hourglassSum(arr):
    # Write your code here
    hourglassSums = []
    for i in range(len(arr)-2):
        for j in range(len(arr[1])-2):
            hourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] +\
                           arr[i+1][j+1] +\
                           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            hourglassSums.append(hourglassSum)
    return max(hourglassSums)