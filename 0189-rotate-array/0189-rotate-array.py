class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k is greater than array length
        if k == 0:
            return

        # 1. Store the last k elements
        temp = nums[n - k:]
        
        # 2. Shift the first n-k elements to the right by k positions
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
            
        # 3. Copy the saved temp elements back to the front
        for i in range(k):
            nums[i] = temp[i]
        temp = nums[n-(k):n]
        for i in range(n - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = temp[i]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna