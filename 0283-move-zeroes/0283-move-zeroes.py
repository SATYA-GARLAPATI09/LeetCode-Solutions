class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        # Find the first zero
        for k in range(len(nums)):
            if nums[k] == 0:
                j = k
                break
                
        # If there are no zeroes, we don't need to do anything
        if j == -1:
            return

        # Start scanning from the first zero onwards
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna