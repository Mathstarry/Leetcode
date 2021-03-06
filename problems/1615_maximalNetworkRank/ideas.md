## 思路与想法
### 方法一：哈希+循环
**思路**：  
首先用一个哈希表记录每一个定点的度，然后用双循环枚举每一对顶点，因为总共只有 100 个顶点，所以 *O*(*N*<sup>2</sup>) 是不会超时的。对于每一对枚举的顶点，如果他们不直接相连，那么这个城市对的网络
秩等于这两个点的度数只和；如果两个顶点直接相连，那么他们的网络秩等于他们的度数之和减去一。然后对所有的网络秩取最大值即可。


**时间复杂度**：*O*(*N*<sup>2</sup>)，*N* 为顶点数  
**空间复杂度**：*O*(*M*)，*M* 为边数
