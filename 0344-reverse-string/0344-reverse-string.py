class Solution:
    def reverseString(self, s: list[str], i: int = 0, r: int = None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize right pointer on the first call
        if r is None:
            r = len(s) - 1
            
        # Base case: when pointers meet or cross
        if i >= r:
            return
        
        # Swap characters in-place
        s[i], s[r] = s[r], s[i]
        
        # Recursive call moving pointers inward
        self.reverseString(s, i + 1, r - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna