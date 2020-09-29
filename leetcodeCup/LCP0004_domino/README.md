# LCP 4. [覆盖](https://leetcode-cn.com/problems/broken-board-dominoes/)  
<font size=5> 难度 `困难` </font>
---

### 题目描述

你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为`1 * 2`的多米诺骨牌，你想把这些骨牌**不重叠**地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。

 

输入：`n, m`代表棋盘的大小；`broken`是一个`b * 2`的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。

输出：一个整数，代表最多能在棋盘上放的骨牌数。

 

示例 1：
```
输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
输出：2
解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）
```

<img src="https://github.com/Mathstarry/Leetcode/blob/master/leetcodeCup/LCP0004_domino/img/LCP4_pic1.png" width = "300" height = "200" alt="" align=center />


示例 2：
```
输入：n = 3, m = 3, broken = []
输出：4
解释：下图是其中一种可行的摆放方式
```

<img src="https://github.com/Mathstarry/Leetcode/blob/master/leetcodeCup/LCP0004_domino/img/LCP4_pic2.png" width = "300" height = "300" alt="" align=center />

限制：

1. `1 <= n <= 8`
2. `1 <= m <= 8`
3. `0 <= b <= n * m`


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/broken-board-dominoes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
