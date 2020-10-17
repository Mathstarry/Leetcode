class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dct = {v: i for i, v in enumerate(nums1)}
        for t in nums2:
            while stack and t > stack[-1]:
                p = stack.pop()
                if p in dct:
                    nums1[dct[p]] = t
            stack.append(t)
        for t in stack:
            if t in dct:
                nums1[dct[t]] = -1
        return nums1
