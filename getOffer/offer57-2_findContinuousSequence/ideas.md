## 思路与想法
### 方法一：数学
**思路**：  
对于给定的数字 `target`，如果存在连续的 `n` 个整数，他们的和为 `target`，那就有 `k*(k+n-1)*n/2 = target' 对于某些 `k`，所以我们只要从 2 到 `target/2` 枚举 `n` 的值，并找到这个
`k` 即可。显然 `2*target/n` 必须是整数，所以 `n` 需要能被 `2*target` 所整除。接下来单独考虑 `n` 的奇偶性：
1. 若 `n` 为奇数，则存在 `t`， 使得 `k*(k+n-1)*n/2 = t * n`，所以只要 `target` 能整除 `n` 并且 `t - (n - 1) / 2 >= 0`，那么 `k` 便是存在的。
2. 若 `n` 为偶数，则存在 `t`， 使得 `k*(k+n-1)*n/2 = t(t+1)*n/2`，所以只要 `2*target/n` 是奇数，并且 `t - n/2 >= 0`，那么 `k` 便是存在的。



**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)
