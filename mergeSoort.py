class Solution:
    def mergeSort(self, nums, low=0, high=None):
        if high is None:
            high = len(nums) - 1
            
        if low >= high:
            return
            
        mid = (low + high) // 2
        self.mergeSort(nums, low, mid)
        self.mergeSort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)
        return nums

    def merge(self, nums, low, mid, high):
        sarr = []
        left = low
        right = mid + 1
        
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                sarr.append(nums[left])
                left += 1
            else:
                sarr.append(nums[right])
                right += 1
                
        while left <= mid:
            sarr.append(nums[left])
            left += 1
            
        while right <= high:
            sarr.append(nums[right])
            right += 1
            
        nums[low:high + 1] = sarr
