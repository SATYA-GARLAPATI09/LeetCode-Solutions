
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm={}
        for i in range (len(nums)):
            ne = target-nums[i]
            if ne in hm:
                return[hm[ne] , i]

            hm[nums[i]]=i


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna