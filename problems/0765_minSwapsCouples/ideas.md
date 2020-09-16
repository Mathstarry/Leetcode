## 思路与想法
### 方法一：贪心
**思路**：  
每次检查一对，若奇数位上与偶数位上是情侣关系，则检查下一对。若不是情侣关系，则往后查找该奇数位上的对象，找到后将其调换过来。  
**时间复杂度**：遍历所有对对复杂度是 *O*(*N*)，为每一对查找其伴侣的复杂度也是 *O*(*N*)，所以总的时间复杂度是 *O*(*N*<sup>2</sup>)。  
**空间复杂度**：*O*(*N*)

### 方法二：并查集
**思路**：  
考虑 `N` 个顶点，其中 `N` 为情侣的对数，每个顶点包含2个人可以理解成每个顶点有2个度，在每队情侣之间连一条边，即若 `x` 与 `x+1` 为情侣，且他们分别在顶点 `i` 和 `j`，则连接顶点`i` 和 `j`。  
显然，我们可以得到一张有多个联通分量的无向图，而使每队情侣坐在一起等价于最后得到一张有 `N` 个联通分量的无向图。那么移动次数就等于 `N` 减去最开始的联通分量数。
那么问题就变成了，给定若干个联通分量，断开任意条边，最终得到 `N` 个联通分量。  

更进一步地，我们不妨考虑把 `rows` 的下标当作人，把 `rows` 的值当作每个人所在的顶点位置，那么我们只需要考虑对于每一对位置：  
1. 若其确实为情侣关系，则无操作，考虑下一对；
2. 若不是情侣关系，则把顶点 `rows[i]//2` 和 `rows[i+1]//2` 连接起来，若在这之前，这两个顶点是不联通的，则 `cnt` 加1，若之前是联通的，则无操作。

上述操作等价于，一开始已经是 `N` 个联通分量，我们连几条边可以得到现在的联通情况，而这增加的边数就是所求的答案。  
**时间复杂度**：遍历所有对对复杂度是 *O*(*N*)，连接边的时间是 *O*(1)，所以总的时间复杂度是 *O*(*N*)。  
**空间复杂度**：*O*(*N*)，这里需要用一个列表存储每个顶点的 `root`，若使用路径压缩，则还需要一个列表存储每个顶点的 `rank`。