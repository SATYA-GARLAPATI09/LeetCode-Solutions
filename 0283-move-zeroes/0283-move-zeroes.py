class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_idx = 0
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
                non_zero_idx += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna