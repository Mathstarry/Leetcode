class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        set1 = {t for t in nums1}
        set2 = {t for t in nums2}
        res = []
        for t in set1:
            if t in set2:
                res.append(t)
        return res
