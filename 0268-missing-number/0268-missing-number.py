class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor1 = 0
        xor2 = 0
        n = len(nums)
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor1 ^= i
            
        # XOR all elements in the array
        for num in nums:
            xor2 ^= num
            
        return xor1 ^ xor2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna