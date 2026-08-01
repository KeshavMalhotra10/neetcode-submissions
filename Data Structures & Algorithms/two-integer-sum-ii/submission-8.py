class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       #another solution is to have a lo and hi pointer
       #and see how close you get to the target over time
       #if the resultant is > target, then move hi left
       #if resultant is < target, move low right

       lo = 0
       hi = len(numbers) - 1
       resultant = -999999999
       while resultant != target:
        resultant = numbers[lo] + numbers[hi]
        if numbers[lo] + numbers[hi] < target:
            lo +=1
        elif numbers[lo] + numbers[hi] > target:
            hi -=1
        else: 
            return [lo+1, hi+1]
        



        