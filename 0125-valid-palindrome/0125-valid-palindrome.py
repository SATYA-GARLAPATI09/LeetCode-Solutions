class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left pointer past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna