class Solution:
    def fib(self, n: int) -> int:
    #base case
        if(n<=1):
            return n
        last = self.fib(n-1)
        slast=self.fib(n-2)
       
        
        return last+slast

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna