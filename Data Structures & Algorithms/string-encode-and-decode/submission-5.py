class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for str in strs:
            s += "aLongSeparateStringNobodyCantReplicate"
            s +=str
        return s
            

    def decode(self, s: str) -> List[str]:
        strList = s.split("aLongSeparateStringNobodyCantReplicate", -1)
        strList.remove("")
        return strList
