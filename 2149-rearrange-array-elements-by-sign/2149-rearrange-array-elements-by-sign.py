class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # we taking the 2 pointers approch 
        # so we take 2 pointers callled pos,neg
        pos =0
        neg =1
        ans = [0]* len(nums)
        for i in range (len (nums)):
            if nums[i]>0:
                ans[pos]=nums[i]
                pos +=2
            else:
                ans[neg] = nums[i]
                neg +=2
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna