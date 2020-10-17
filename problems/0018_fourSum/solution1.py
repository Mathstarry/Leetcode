class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n, res = len(nums), []
        for i in range(n-3):
            # 四数之和过大了，剪枝
            if sum(nums[i:i+4]) > target: break
            # 前者用以去重，后者四数之和过小，剪枝
            if i > 0 and nums[i] == nums[i-1] or nums[i]+sum(nums[n-3:]) < target: continue
            for j in range(i+1, n-2):
                # 以下2句，分别是四数之和过小，剪枝；去重
                if nums[i]+nums[j]+sum(nums[n-2:]) < target: continue
                if j > i+1 and nums[j] == nums[j-1]: continue
                l, r, v = j + 1, n - 1, target - nums[i] - nums[j]
                while l < r:
                    # 四数之和过大或过小，剪枝
                    if 2 * nums[l] > v or 2 * nums[r] < v: break
                    elif nums[l] + nums[r] == v:
                        if l == j+1 or nums[l] != nums[l-1] or r == n-1 or nums[r] != nums[r+1]:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l, r = l + 1, r - 1
                    elif nums[l] + nums[r] > v:
                        r -= 1
                    elif nums[l] + nums[r] < v:
                        l += 1
        return res
