class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dct = {p[0]: i for i, p in enumerate(pieces)}
        i = 0
        while i < len(arr):
            if arr[i] in dct:
                p = pieces[dct[arr[i]]]
                l = len(p)
                if arr[i:i+l] != p:
                    return False
                i += l
            else:
                return False
        return True
