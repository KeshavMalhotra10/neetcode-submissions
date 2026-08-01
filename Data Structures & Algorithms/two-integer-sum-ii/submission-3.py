class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 1 #starting index
        p2 = p1 + 1 #second index
        while(p1 != p2):
            if numbers[p1-1] + numbers[p2-1] == target:
                return [p1 , p2]
            if p2 == len(numbers):
                p1 = p1 + 1
                p2 = p1 + 1
            else:
                p2 = p2 + 1


        