class Solution:
    def largestElement(self, nums):
        large = nums[0]
        for i in  range (len(nums)):
            if nums[i]>large:
                large = nums[i]

        return large
        
