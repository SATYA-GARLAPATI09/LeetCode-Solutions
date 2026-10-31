class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count =0
        for i in range(1,min(a,b)+1):
            if a%i==0 and b%i==0:
                count = count+1

        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna