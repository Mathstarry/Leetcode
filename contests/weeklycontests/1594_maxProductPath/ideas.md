## 思路与想法
### 方法一：动态规划
**思路**：  
队对于元素全为正数的情况，只要建立一个二维数组用于存储最大值即可，由于这里元素可以为负，所以对于每一个位置，我们要同时维护最大值和最小值。
首先建立一个大小为 `n x m x 2` 的三维数组 `dp`，然后初始化其第一行和第一列，每个位置两个元素，分别记录最大值和最小值，对于首行首列而言，其最大小值为同一个数，即前i项的乘积。
然后从 `(1, 1)` 位置开始遍历 `grid`，对于每一个位置 `(i, j)`，我们取出其上方和左边的 `dp` 数组中的最大小值 共4个数字，令每一个数字都乘以 `grid[i][j]`，在新的4个数字中选取最大小值，
作为 `dp[i][j]` 的值。

需要注意的是，在遍历 `grid` 的过程中还要判断是否出现过 0，如果出现过 0，并且计算得到 `dp` 最末尾的元素的最大值为负，此时应输出 `0` 而非 `-1`。

**时间复杂度**：*O*(*N*<sup>2</sup>)  
**空间复杂度**：*O*(*N*<sup>2</sup>)
