class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l,r =0,0
        res,total=0,0
        for r in range (len(nums)):
            total += nums[r]
            if (total +k < (r-l+1)*nums[r]):
                total -=nums[l]
                l +=1

            res = max(res,(r-l+1))
            r +=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna