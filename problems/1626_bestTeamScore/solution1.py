class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        nums = []
        for i in range(len(ages)):
            nums.append([ages[i], scores[i]])
        nums.sort()
        res, dp = 0, [[0, 0] for _ in range(len(nums))]
        for i in range(len(dp)):
            dp[i] = [nums[i][1], nums[i][1]]
        for i in range(len(dp)):
            for j in range(i):
                if nums[i][1] >= dp[j][0] and dp[i][1] < dp[j][1] + nums[i][1]:
                    dp[i] = [nums[i][1], dp[j][1] + nums[i][1]]
            res = max(res, dp[i][1])
        return res
