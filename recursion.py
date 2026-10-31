class Solution:
    def printNumbers(self, n):
        # Base case: if n is 0, stop recursion
        if n == 0:
            return
        
        # First, recursively call for n - 1
        self.printNumbers(n - 1)
        
        # Then print n (this ensures numbers print from 1 to n)
        print(n)
