class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min =i
            for j in range (i+1,len(nums)):
                if nums[j]<nums[min]:
                    min=j
            nums[min],nums[i]=nums[i],nums[min]
        return nums
