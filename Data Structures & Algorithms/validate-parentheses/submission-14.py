class Solution:
    def isValid(self, s: str) -> bool:
        keyVal = {"}":"{", "]":"[", ")":"(" } #key value pair
        if len(s) == 1:
            return False
        if s[0] in keyVal:
            return False
        st = []
        for bracket in s:
            if bracket not in keyVal:
                st.append(bracket)
            elif st and st[-1] == keyVal[bracket]:
                st.pop()
            else:
                return False
        if st:
            return False
        return True

            

        