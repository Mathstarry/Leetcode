## 思路与想法
### 方法一：双指针
**思路**：  
快慢指针可以解决这个问题，定义一个快指针，每次向前行进2格，定义一个慢指针，每次向前行进1格，当快指针为空时，表明链表无环，返回 `False`。当快慢指针相遇时，表明链表有环，返回 `True`。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*1*)