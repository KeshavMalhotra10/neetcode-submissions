class Solution:
    def isPalindrome(self, s: str) -> bool:
        #have left and right pointers
        #compare left and right to see if they are equal
        #ignore whitespace or other punctuation 

        #lowercase 
        s = s.lower()
        left = 0
        right = len(s) -1

        for i in range(len(s) - 1):
            if s[left] == s[right]:
                left+=1
                right-=1
            elif s[left].isalnum() == False:
                left+=1
            elif s[right].isalnum() == False:
                right-=1
            else:
                return False
        return True
            

        
        

        

        