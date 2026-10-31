class Solution:
  
    def NnumbersSum(self, N, total=0):

        if N == 0:
            return total
        
        total = total + N
        return self.NnumbersSum(N - 1, total)
