## 思路与想法
### 方法一：双指针
**思路**：  
使用两个指针 `i`, `j`，先移动指针 `j`，每次都判断 `j` 指向的字母是否出现在当前 `[i,j)` 指向的子串中，若有，则向右移动 `i`，直到区间中无与 `j` 指向的字母重复的字母为止。若没有，则继续向右移动指针 `j`。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)