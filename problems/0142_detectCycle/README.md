# 142. [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)  
<font size=5> 难度 `中等` </font>
---

### 题目描述

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 `null`。

为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。**注意，`pos` 仅仅是用于标识环的情况，并不会作为参数传递到函数中。**

说明：不允许修改给定的链表。

进阶：

* 你是否可以使用 `O(1)` 空间解决此题？
 

示例 1：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0142_detectCycle/img/142_pic1.png" width = "400" height = "130" alt="" align=center />


```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```
示例 2：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0142_detectCycle/img/142_pic2.png" width = "200" height = "120" alt="" align=center />


```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```
示例 3：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0142_detectCycle/img/142_pic3.png" width = "80" height = "70" alt="" align=center />


```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```
 

提示：

* 链表中节点的数目范围在范围 `[0, 104]` 内
* `-105 <= Node.val <= 105`
* `pos` 的值为 `-1` 或者链表中的一个有效索引

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。