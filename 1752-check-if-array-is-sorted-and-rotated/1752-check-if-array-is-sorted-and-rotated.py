class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i - 1] > nums[i] for i in range(len(nums))) < 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna