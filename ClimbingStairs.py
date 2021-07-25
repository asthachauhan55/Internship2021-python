class Solution:
    def climbStairs(self, n: int) -> int:
        path = {1: 1,2: 2,3: 3} 
        '''Dictionary containing the data we already know'''
        
        for x in range(4, n+1):
            path[x]= path[x-1] + path[x-2]
        return(path[n])
