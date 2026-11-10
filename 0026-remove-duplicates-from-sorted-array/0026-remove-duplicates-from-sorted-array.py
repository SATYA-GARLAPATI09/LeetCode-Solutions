class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k =0
        for i in range(1,len(nums)):
            if nums[i]!=nums[k]:
                nums[k+1]=nums[i]
                k +=1

        return k+1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna