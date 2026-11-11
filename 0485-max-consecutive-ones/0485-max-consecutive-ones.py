class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxi =0
        cnt =0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt +=1
                maxi = max(maxi,cnt)
            else:
                cnt=0

        return maxi


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna