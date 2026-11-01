class Solution:
    def countFrequencies(self, nums):
        freq_map = {}
        
        # Count frequencies manually using a dictionary
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
            
        # Convert the dictionary into the required list of [element, frequency] pairs
        output = [[num, count] for num, count in freq_map.items()]
        
        return output
