class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range (len(nums)+1):
            flag =0
            for j in range (len(nums)):
                if nums[j]==i:
                    flag=1
                    break
            if flag ==0:
                return i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna