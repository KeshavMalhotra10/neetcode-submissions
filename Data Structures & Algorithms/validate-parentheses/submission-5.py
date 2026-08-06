class Solution:
    def isValid(self, s: str) -> bool:
        #implement a hashmap closeToOpen
        closeOpen = {"}":"{", "]":"[", ")":"("}
        st = [] #this is the stack

        for bracket in s:
            if bracket in closeOpen:
                if st and st[-1] == closeOpen[bracket]:
                    st.pop()
                else:
                    return False
            else:
                st.append(bracket)
            
        if st:
            return False
        return True
        
        
    


          


        
        



        