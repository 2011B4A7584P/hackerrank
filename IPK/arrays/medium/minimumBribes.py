def minimumBribes(queue):
    
    bribes = 0
    
    for i in range(len(queue)):
        
        if queue[i] - (i+1) > 2:
            print('Too chaotic')
            return
        
        for j in range(max(0, queue[i]-2), i):
            if queue[j] > queue[i]:
                bribes += 1
    
    print(bribes)

'''
minimumBribes([2,1,5,3,4])    #answer  : 3
minimumBribes([2,5,1,3,4])    #answer  : Too chaotic
minimumBribes([1,2,5,3,7,8,6,4])  #answer  : 7
'''