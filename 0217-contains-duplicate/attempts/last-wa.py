class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        cnt =0

        for i in range(n):
            for j in range (i+1,n):
                if nums[i]==nums[j]:
                    cnt +=1
        if cnt ==0:
            return False
        else:
            return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna