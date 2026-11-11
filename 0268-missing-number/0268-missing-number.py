class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor_sum = 0
        n = len(nums)
        
        for i, num in enumerate(nums):
            xor_sum ^= i ^ num  # XOR the index and the array element together
            
        return xor_sum ^ n      # Finally, XOR the missing upper bound `n`

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna