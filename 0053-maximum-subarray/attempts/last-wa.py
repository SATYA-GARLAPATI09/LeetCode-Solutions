class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize both to the first element to correctly handle 
        # single-element arrays and arrays with all negative numbers.
        current_sum = 0
        maxi = 0
        
        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            maxi = max(maxi, current_sum)
            
        return maxi

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna