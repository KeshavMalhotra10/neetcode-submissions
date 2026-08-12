class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0] #dont ever just arbritarily set a number


        while l <= r: #why less than or EQUAL and not just less than
            if nums[l] < nums[r]:
                res = min(res, nums[l]) #min function is useful
                break

            mid = (l + r) // 2
            res = min(res, nums[mid]) #again this min statement helpful
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1

        return res
            

        