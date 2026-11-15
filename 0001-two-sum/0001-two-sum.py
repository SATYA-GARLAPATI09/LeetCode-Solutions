
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash_map = {}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in hash_map:
                return [hash_map[needed], i]

            hash_map[nums[i]] = i


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna