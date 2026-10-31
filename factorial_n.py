class Solution:
    def recurssion(self, n):
        # Base case
        if n == 0:
            return 1
            
        # Recursive call for factorial
        return n * self.recurssion(n - 1)
