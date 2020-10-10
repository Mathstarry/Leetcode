## 思路与想法
### 方法一：遍历
**思路**：  
先对数组作降序排序，然后从 1 到 N 进行枚举，如果恰好存在某个 x，刚好使得排序后的数组前 x 位大于等于 x，且之后的数字都严格小于 x，那么返回 x，否则返回 -1。


**时间复杂度**：*O*(*N* * *log*(*N*))  
**空间复杂度**：*O*(*1*)