class Solution:
    def isValid(self, s: str) -> bool:
        keyVal = {"}":"{", "]":"[", ")":"(" } #key value pair
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

            

        