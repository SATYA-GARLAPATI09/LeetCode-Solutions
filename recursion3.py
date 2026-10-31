class Solution:
    def printNumbers(self, n):
        #base case 
        if n ==0 :
            return True
        #printNumbers
        print(n)
        #recurssion calling
        self.printNumbers(n-1)
    
