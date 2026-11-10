class Solution:
    def mergeSort(self, nums, low, high):

        # Base case
        if low >= high:
            return

        mid = (low + high) // 2

        # Divide left half
        self.mergeSort(nums, low, mid)

        # Divide right half
        self.mergeSort(nums, mid + 1, high)

        # Merge both halves
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):

        sarr = []

        left = low
        right = mid + 1

        # Compare elements from both halves
        while left <= mid and right <= high:

            if nums[left] <= nums[right]:
                sarr.append(nums[left])
                left += 1

            else:
                sarr.append(nums[right])
                right += 1

        # Add remaining left elements
        while left <= mid:
            sarr.append(nums[left])
            left += 1

        # Add remaining right elements
        while right <= high:
            sarr.append(nums[right])
            right += 1

        # Copy sorted elements back into original array
        nums[low:high + 1] = sarr

# Driver code
nums = [38, 27, 43, 3, 9, 82, 10]

obj = Solution()
obj.mergeSort(nums, 0, len(nums) - 1)

print(nums)
