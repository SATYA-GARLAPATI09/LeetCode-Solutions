
class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        el = None
        cnt = 0

        for i in range(len(nums)):

            if cnt == 0:
                el = nums[i]
                cnt = 1

            elif nums[i] == el:
                cnt += 1

            else:
                cnt -= 1

        cnt1 = 0

        for i in range(len(nums)):
            if nums[i] == el:
                cnt1 += 1

        if cnt1 > (len(nums) // 2):
            return el


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna