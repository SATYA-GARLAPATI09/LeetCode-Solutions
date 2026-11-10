class Solution:
    def bubbleSort(self, nums):
        for i in range(len(nums)):
            count =0
            for j in range(len(nums)-(i+1)):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    count +=1
            if count ==0:
                break
        return nums          
