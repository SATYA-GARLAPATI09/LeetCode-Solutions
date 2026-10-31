class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Initialize counter for common factors
        count = 0
        # Iterate through all possible factors up to the smaller of a and b
        # For each i, check if it divides both a and b
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                count = count + 1
        # Time Complexity: O(min(a, b)) – we check each integer up to the smaller number
        # Space Complexity: O(1) – only a few integer variables are used
        # Note: A slightly more optimal approach is to compute gcd(a, b) and count its divisors,
        # which runs in O(sqrt(gcd(a, b))) time. The current solution is sufficient for the given constraints.
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna