# 144. [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)  
<font size=5> 难度 `中等` </font>
---

### 题目描述

给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

 

示例 **1**：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0144_preorderTraversal/img/144_pic1.png" width = "235" height = "300" alt="" align=center />

```
输入：root = [1,null,2,3]
输出：[1,2,3]
```
示例 **2**：
```
输入：root = []
输出：[]
```
示例 **3**：
```
输入：root = [1]
输出：[1]
```
示例 **4**：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0144_preorderTraversal/img/144_pic2.png" width = "235" height = "200" alt="" align=center />

```
输入：root = [1,2]
输出：[1,2]
```
示例 **5**：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0144_preorderTraversal/img/144_pic3.png" width = "235" height = "200" alt="" align=center />

```
输入：root = [1,null,2]
输出：[1,2]
```

提示：

* 树中节点数目在范围 `[0, 100]` 内
* `-100 <= Node.val <= 100`

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
