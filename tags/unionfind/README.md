# 并查集
并查集主要用于处理图的联通性问题。

并查集一般有两种结构可以选择：  
* 一种是[基础版的并查集](https://github.com/Mathstarry/Leetcode/blob/master/tags/unionfind/unionfind1.py)，
一个成员变量 `root`，用以记录每个结点的父节点，两个方法，`find(p:node)` 和 `union(p:node, q:node)`，
前者用以返回某个节点的根节点(祖结点)，后者用以将两个结点连在一起。
* 第二种是[压缩路径的并查集](https://github.com/Mathstarry/Leetcode/blob/master/tags/unionfind/unionfind-path-compression.py)，
相较于第一种，需要再添加一个成员变量 `rank`，用以记录每个联通分量的高度，因为每一个联通分量都是一棵树，记录高度的目的是每次连接两棵原本不联通的树的时候，
我们每次都是把高度较小的树连在高度较大的树的根节点下，这样可以最大限度地减少树的高度的增加，加快 `find` 时的速度，同时在 `union` 操作时，也比方法一多一些操作。  

note: 另一个可选的操作是增加 `isConnected(p:node, q:node)` 方法，用以快速返回两个结点是否相连。同时还可以根据题意增加或修改变量和方法，
在实际使用中，不一定去单独定义一个 `unionfind` 类，有可能是直接定义在核心函数里。



## 并查集题目

### 简单


---
### 中等
[684. 冗余连接](https://github.com/Mathstarry/Leetcode/tree/master/problems/0684_findRedundantConnection)

---
### 困难
[685. 冗余连接II](https://github.com/Mathstarry/Leetcode/tree/master/problems/0685_findRedundantDirectedConnection)  
[765. 情侣牵手](https://github.com/Mathstarry/Leetcode/tree/master/problems/0765_minSwapsCouples)
