class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def cum(v, n):
            if n == 0: return 0
            return (v + v - n + 1) * n // 2

        res, MOD, n = 0, 10 ** 9 + 7, len(inventory)
        inventory.sort(reverse=True)
        for i in range(n-1):
            diff = inventory[i] - inventory[i+1]
            if orders >= diff * (i+1):
                res += cum(inventory[i], diff) * (i+1)
                orders -= diff * (i + 1)
            else:
                d, r = orders // (i+1), orders % (i+1)
                res += cum(inventory[i], d) * (i+1) + cum(inventory[i] - d, 1) * r
                orders = 0
            res %= MOD
        if orders > 0:
            d, r = orders // n, orders % n
            res += cum(inventory[-1], d) * n + cum(inventory[-1] - d, 1) * r
            res %= MOD
        return res
