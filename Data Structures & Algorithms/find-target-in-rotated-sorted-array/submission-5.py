class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) -1
        res = -1 #we will just return -1 if no result found

        while l <= r: 
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            
            #check for whether you are in left sorted portion or right sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

# right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1 


        return -1

        