## 思路与想法
### 方法一：动态规划
**思路**：  
首先我们对词典进行预处理。记 `m` 为词典中每个单词的长度，`s` 为目标字符串的长度。定义一个长度为 `m` 的列表，列表中的元素是字典，列表的第 `i` 位表示词典所有字符串第 `i` 位字母的频率统计。比如 
`dct[i][k]` 表示词典的字符串中第 `i` 位出现字母 `k` 的频率。预处理完之后可以使用动态规划进行方案数的求解。  
我们用 `dp[i][j]` 表示词典中所有字符串的前 `i` 位能组成目标字符串前 `j` 位的方案数。 `dp[i][0]` 表示词典中所有字符串的前 `i` 位能组成空字符串的方案数，显然为 1，也即全部不取，所以我们将这
类值全部初始化为 1，其余值初始化为 0。状态转移方程为 `dp[i][j] = dp[i-1][j-1] * dct[i-1][t] + dp[i-1][j]`, 其中 `t` 表示目标字符串第 `j-1` 位的字母(从 0 开始索引)。该式子前半部分表示，
对于词典的前 `i-1` 位和目标字符串的前 `j-1` 位，已知有 `dp[i-1][j-1]` 种方案数，现在对于目标字符串的第 `j` 位，词典中的第 `i` 位上有 `dct[i-1][t]` 个满足条件的字母，那么 `dp[i][j]` 就
等于这两者之积。而后半部分表示，如果词典的前 `i-1` 位已经组成了目标字符串的前 `j` 位，那么我们第 `i` 位不取，这样仍可以得到 `dp[i][j]`，所以最终需要将两者相加来作为 `dp[i][j]` 的值。


**时间复杂度**：*O*(*ms*)，其中 `m` 为词典中每个单词的长度，`s` 为目标字符串的长度  
**空间复杂度**：*O*(*ms*)
