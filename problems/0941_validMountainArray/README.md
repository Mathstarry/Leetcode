# 941. [有效的山脉数组](https://leetcode-cn.com/problems/valid-mountain-array/)  
<font size=5> 难度 `简单` </font>
---

### 题目描述

给定一个整数数组 `A`，如果它是有效的山脉数组就返回 `true`，否则返回 `false`。

让我们回顾一下，如果 `A` 满足下述条件，那么它是一个山脉数组：

* `A.length >= 3`
* 在   0 < i < A.length - 1   条件下，存在   i  使得：
  * A[0] < A[1] < ... A[i-1] < A[i]
  * A[i] > A[i+1] > ... > A[A.length - 1]
 
<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0941_validMountainArray/img/941_pic.png" width = "600" height = "400" alt="" align=center />


 

示例 1：
```
输入：[2,1]
输出：false
```
示例 2：
```
输入：[3,5,5]
输出：false
```
示例 3：
```
输入：[0,3,2,1]
输出：true
```

提示：

1. `0 <= A.length <= 10000`
2. `0 <= A[i] <= 10000 `

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
