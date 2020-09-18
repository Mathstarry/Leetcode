## 思路与想法

### 方法一：启发式方法+并查集
**思路**：  
分类讨论图中存在根节点与不存在根节点的情况。前者必定存在入度为2的结点，只要去掉该节点在环上的一条入边即可；后者去掉成环所添加的最后一条边即可，
方法与[684. 冗余连接 方法一](https://github.com/Mathstarry/Leetcode/edit/master/problems/0684_findRedundantConnection/ideas.md)相同。  
[详细题解](https://leetcode-cn.com/problems/redundant-connection-ii/solution/qi-fa-shi-fang-fa-bing-cha-ji-py3su-du-96yi-shang-/)

**时间复杂度**：最差情况下，前者 *O*(*N*)，后者 *O*(*N*<sup>2</sup>)。  
**空间复杂度**：*O*(*N*)。
