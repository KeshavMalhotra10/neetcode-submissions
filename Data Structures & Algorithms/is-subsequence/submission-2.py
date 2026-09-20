class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #recursive solution
        def rec(i,j):
            if i == len(s): #we checked all letters needed
                return True 
            if j == len(t): #no letter left to advance i
                return False
            elif s[i] != t[j]:
                 return rec(i, j+1)
            return rec(i+1, j+1)
        return rec(0,0)
    


    
            
            

        

    
        