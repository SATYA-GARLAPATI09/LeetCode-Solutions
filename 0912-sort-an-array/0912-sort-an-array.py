class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: arrays with 0 or 1 element are already sorted
        if len(nums) <= 1:
            return nums
        
        # Split the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Merge the sorted halves back together
        return self.merge(left_half, right_half)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        sorted_array = []
        i = j = 0
        
        # Compare elements from both halves and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
                
        # Append any remaining elements
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna