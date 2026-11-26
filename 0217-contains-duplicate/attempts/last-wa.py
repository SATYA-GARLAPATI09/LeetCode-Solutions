class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap ={}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[i] = nums[i]
        return False


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna