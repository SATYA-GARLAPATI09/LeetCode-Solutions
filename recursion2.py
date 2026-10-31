class Solution:
  def recurssion(self,n):
    #base case
    if n ==0:
      return True
            # First, recursively call for n - 1
    self.recurssion (n-1)
    # printing the name 
    print("Satya")
  
