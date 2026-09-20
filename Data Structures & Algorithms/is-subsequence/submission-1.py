class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        solution 1: hashmap time o(n), space o(n)
        simply store all the values of t in a freqmap, and see if it is possible to make the other word 
        update char freqs based on usage, oh cant disturb positions

        Solution 2: two pointer 
        keep a pointer on s and one on t, and then just keep moving through t while the value s is looking for is not found
        If we satify s return true, else Fasle
        '''
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        
        return True if i == len(s) else False
    
            
            

        

    
        