class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def merge(nums, start, mid, end, lst):
            for j in range(mid + 1, end + 1):
                lst.append(nums[j])
            i, j, k = mid, len(lst) - 1, end
            while j >= 0:
                if i < start or lst[j] >= nums[i]:
                    nums[k] = lst[j]
                    j -= 1
                else:
                    nums[k] = nums[i]
                    i -= 1
                    self.count += j + 1
                k -= 1
            lst.clear()

        def mergeSort(nums, start, end, lst):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, lst)
            mergeSort(nums, mid + 1, end, lst)
            merge(nums, start, mid, end, lst)

        mergeSort(nums, 0, len(nums) - 1, [])
        return self.count
        
