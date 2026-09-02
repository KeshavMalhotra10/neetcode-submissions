class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for str in strs:
            s += "separate"
            s +=str
        return s
            

    def decode(self, s: str) -> List[str]:
        strList = s.split("separate", -1)
        strList.remove("")
        return strList
