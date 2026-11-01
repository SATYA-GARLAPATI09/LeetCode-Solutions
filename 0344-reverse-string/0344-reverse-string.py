class Solution:
    def reverseString(self, s: list[str], i: int = 0, r: int = None) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Time Complexity: O(n) where n = len(s)
        # Space Complexity: O(n) due to recursion stack (call depth). For O(1) extra space, consider an iterative two-pointer loop.
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
        # After this recursion finishes, the entire list s will be reversed in-place.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna