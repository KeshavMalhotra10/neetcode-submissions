class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l < r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
            if s[r].isalnum() and s[l].isalnum() and s[r] != s[l]:
                return False
            if s[r] == s[l]:
                l+=1
                r-=1
        return True
