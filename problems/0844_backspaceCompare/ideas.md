## 思路与想法
### 方法一：栈
**思路**：  
对两个字符串执行相同的操作，把他们放入一个栈中，遇到 `#` 就出栈，否则，入栈，执行完这个操作之后，如果两个栈中的字符串顺序相同，那么返回 `True`，否则返回 `False`。

**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)