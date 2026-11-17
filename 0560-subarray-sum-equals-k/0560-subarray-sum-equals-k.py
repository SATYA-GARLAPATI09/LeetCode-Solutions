class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Hash map to store frequency of prefix sums
        # Initialize with {0: 1} to handle subarrays starting from index 0
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Check if (current_sum - k) exists in our map
            diff = current_sum - k
            if diff in prefix_sums:
                count += prefix_sums[diff]
                
            # Add current_sum to the map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna