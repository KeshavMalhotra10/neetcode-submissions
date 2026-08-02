class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, value in enumerate(nums):
            lo = index +1
            hi = len(nums) -1

            if index > 0 and nums[index] == nums[index-1]:
                continue

            while lo < hi:
                threeSum = nums[index] + nums[lo] + nums[hi]
                if threeSum < 0:
                    lo +=1
                elif threeSum >0:
                    hi -=1
                elif threeSum == 0:
                    result.append([nums[index], nums[lo], nums[hi]])
                    lo+=1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo+=1
        return result

        
        