## 思路与想法
### 方法一：动态规划
**思路**： 
`dp[i][j]` 表示第 `i` 位为 `j` 时总共的方案数，均从 0 开始计数， `j = 0, 1, 2, 3, 4` 分别表示取 `a, e, i, o, u` 的情形。那么新的一位放置某个字母之后总的方案数等于前一位放置可放置的字母
之后方案数之和。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)
