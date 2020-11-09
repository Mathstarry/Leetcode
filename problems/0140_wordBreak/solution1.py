class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dct = collections.defaultdict(list)
        for word in wordDict:
            dct[word[0]].append(word)
        self.res = []
        
        @lru_cache(None)
        def trackback(t, idx):
            if idx == len(s):
                tmp = copy.deepcopy(t[1:])
                self.res.append(tmp)
                return
            if s[idx] not in dct:
                return
            nums = dct[s[idx]]
            for word in nums:
                l = len(word)
                if s[idx:idx+l] != word: continue
                ans = " ".join([t, word])
                trackback(ans, idx+l)

        dp = [0] * (len(s) + 1)
        dp[0], r = 1, 0
        for i in range(len(s)):
            if s[i] not in dct:
                if i < r: continue
                else: break
            for word in dct[s[i]]:
                l = len(word)
                if i + l < len(dp) and s[i:i+l] == word:
                    dp[i + l] += dp[i]
                    r = max(r, i + l)
        flag = True if dp[-1] > 0 else False
        if flag: trackback("", 0)
        return self.res
