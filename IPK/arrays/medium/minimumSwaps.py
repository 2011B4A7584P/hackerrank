def minimumSwaps(arr):

    swaps = 0

    # Case 1 : Array size is either 0 or 1
    if len(arr) in [0,1] or arr == list(range(1, len(arr)+1)):
        return 0
    
    # Case 2 : Array size is 2
    elif len(arr) == 2:
        return 1
        
    # Case 3 : Array size > 3        
    else:
        for index, value in enumerate(arr):
            
            if value == index + 1:
                continue
            
            else:
                arr[index], arr[value-1] = arr[value-1], arr[index]
                swaps += 1         
        
    return swaps + minimumSwaps(arr)

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))#5
print(minimumSwaps([4, 3, 1, 2]))#3
print(minimumSwaps([2, 3, 4, 1, 5]))#3