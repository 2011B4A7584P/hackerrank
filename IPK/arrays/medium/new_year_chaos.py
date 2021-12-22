# Problem Title : New Year Chaos
# Level : MEDIUM

# Complete the 'minimumBribes' function below
# The function accepts INTEGER_ARRAY q as parameter

def minimumBribes(queue):
    
    # Write your code here
    bribes = 0
  
    i = len(queue)-1
    while i>=0:
        
        # Case where no bribe has happened
        if queue[i] == i+1:
            i -= 1
            continue
            
        # Case where too many (more than 2) bribes have happened    
        elif queue[i] - (i+1) > 2:
            print('Too chaotic')
            return

        else:
            # bribe has happened
            if i-1 >= 0 and queue[i-1] == i + 1:
                bribes += 1
                queue[i-1], queue[i] = queue[i],queue[i-1]
                
            elif i-2 >= 0 and queue[i-2] == i + 1:
                bribes += 2
                queue[i-1], queue[i-2] = queue[i-2], queue[i-1]
                queue[i-1], queue[i] = queue[i], queue[i-1]
                
        i -= 1        
    print(bribes)
    
minimumBribes([2,1,5,3,4])    #answer  : 3
minimumBribes([2,5,1,3,4])    #answer  : Too chaotic
minimumBribes([1,2,5,3,7,8,6,4])  #answer  : 7