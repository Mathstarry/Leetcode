## 思路与想法
### 方法一：双指针
**思路**：  
首先将指针 `i` 定位在第一个点，让指针 `j` 遍历整个数组，同时计算 `i` 与 `j` 指针指向的元素组成的分数，如果对于某个 `j`，有 `A[i] - A[j] <= j - i`，那么我们将 `i` 更新为 `j`。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*1*)
