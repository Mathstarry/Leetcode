## 思路与想法
### 方法一：单调栈
**思路**：  
与[下一个更大元素 I](https://github.com/Mathstarry/Leetcode/tree/master/problems/0496_nextGreaterElement)相同，这里只需要维护一个单调递减栈，栈中记录的是每个元素的索引，当当前元素
比栈尾索引指向的元素要大时，记录两个索引之差到结果数组中该索引对应的位置即可。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)
