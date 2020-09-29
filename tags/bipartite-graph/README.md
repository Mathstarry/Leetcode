# 二分图
这里主要介绍二分图的最大匹配问题，以及匈牙利算法。


**二分图**:  
图中所有的顶点可以分成两部分，每个点只与另一部分中的若干个点有连接，同一部分内的点不会有任何连接。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic1.png" width = "215" height = "275" alt="" align=center />


**匹配**:  
将两部分中的部分点连接起来，并且满足任意两条边之间没有公共顶点，的边的集合称为二分图的一个匹配。匹配不一定要使所有顶点都有相关边，所以匹配可以有许多种。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic2.png" width = "215" height = "275" alt="" align=center />

**增广路径**:  
对于图 2 中的匹配 M，如果我们能找到一条路径 P: `D-2-B-3-C-4`，使得该路径上交替出现在匹配 M 中的边和不在匹配 M 中的边，则称这条路径为匹配 M 的一条增广路径。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic3.png" width = "215" height = "275" alt="" align=center />

**最大匹配**:  
如果在一个匹配中，不能找到关于这个匹配的一条增广路径，那么我们称这个匹配为这个二分图的一个最大匹配，需要注意的是，最大匹配不一定是唯一的(不妨考虑完全图)。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic4.png" width = "215" height = "275" alt="" align=center />

**匈牙利算法**:  
目的: 找到一个关于改二分图的最大匹配。  
方法: 以其中一个部分为研究对象，对该部分中的每一个点，依次寻找其可以建立连接的点，如果对于某个点，其可以连接的点都已经被别的点匹配，那么便寻找以该点为其中一个顶点的增光路，如果可以找到，
那么将增广路径上原先匹配的边全部去掉，连接上增广路径上原先未被连接的边，这样得到的边一定比之前的多 1。如果找不到增广路径，则让该点孤立。  
依次对该部分所有点进行上述操作，便可以得到关于该二分图的一个最大匹配。

例题: 寻找图 1 的一个最大匹配。  
1. 该图可以被分为左侧(拉丁字母部分)和右侧(数字部分)，现在以左侧部分为研究对象。  
2. 按顺序首先考虑 A，A 可以与数字 1 或者 2 匹配，因为 1 尚未被匹配，所以连接 `A-1`。  
3. 接下来考虑 B，B 可以与数字 2 或者 3 匹配，因为 2 尚未被匹配，所以连接 `B-2`。
4. 考虑顶点 C，C 可以与数字 3 或者 4 匹配，因为 3 尚未被匹配，所以连接 `C-3`。
5. 考虑顶点 D，D 可用于数字 2 匹配，因为 2 已经与 B 匹配，所以需要尝试寻找增广路径。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic5.png" width = "650" height = "275" alt="" align=center />

6. 去掉边 `B-2`，连接 `D-2`。
7. B 可以与数字 2 或者 3 连接，因为在目前的路径(`D-2`)上已经包含了数字 2，所以不能连接 `B-2`，考虑去掉边 `C-3`，连接 `B-3`。
8. C 可以与数字 3 或者 4 连接，因为在目前的路径(`D-2-B-3`)上已经包含了数字 3，所以不能连接 `C-3`，而 4 尚未被匹配，所以连接 `C-4`，至此，我们已经找到了一条增广路径 `D-2-B-3-C-4`。
9. 目前图中所有顶点均已匹配，且无法找到增广路径，所以目前的匹配是该图的一个最大匹配。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/tags/bipartite-graph/img/pic6.png" width = "650" height = "275" alt="" align=center />


## 最大匹配题目

### 简单


---
### 中等


---
### 困难
[LCP 4. 覆盖](https://github.com/Mathstarry/Leetcode/tree/master/leetcodeCup/LCP0004_domino)  
