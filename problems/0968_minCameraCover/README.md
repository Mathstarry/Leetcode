# 968. [监控二叉树](https://leetcode-cn.com/problems/binary-tree-cameras/)  
<font size=5> 难度 `困难` </font>
---

### 题目描述

给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。

 

示例 1：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0968_minCameraCover/img/968_pic1.png" width = "150" height = "200" alt="" align=center />

```
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。
```
示例 2：

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0968_minCameraCover/img/968_pic2.png" width = "150" height = "300" alt="" align=center />

```
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。
```
提示：

1. 给定树的节点数的范围是 `[1, 1000]`。
2. 每个节点的值都是 0。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-cameras
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
