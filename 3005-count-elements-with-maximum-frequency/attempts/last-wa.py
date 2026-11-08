class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*15
        for i in nums:
            freq[i] += 1
            
        max_freq = max(freq)
        
        total_frequencies = 0
        for f in freq:
            if f == max_freq:
                total_frequencies += f
                
        return total_frequencies

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna