## 思路与想法
### 方法一：动态规划
**思路**：  
状态: `dp[i][0]` 表示当第 `i` 个叶子为红色时需移动的最少次数；`dp[i][1]` 表示当第 `i` 个叶子为黄色时需移动的最少次数；`dp[i][2]` 表示当第 `i` 个叶子为黄色后的红色时需移动的最少次数。
转移: 叶子的颜色只会从 0 到 1 到 2 逐步变化，不会逆变化，也不会跨越变化。若当前叶子颜色不变，则计数无变化，否则，计数加一。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(1)
