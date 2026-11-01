class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())

        def check(i, r):
            if i >= r:
                return True

            if s[i] != s[r]:
                return False

            return check(i + 1, r - 1)

        return check(0, len(s) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna