## 思路与想法
### 方法一：回溯
**思路**：  

N 皇后是一道经典的回溯题，由棋盘的对称性，我们只需要研究棋盘一侧的棋子摆放即可，这里我们研究左侧棋子的摆放。由于每行每列上均只能有一个棋子，所以事实上当第一行的棋子位置确定时，其余行棋子的位置都可
由回溯得到，我们只需要研究第一行左侧棋子的摆放法即可。回溯的规则还可以更加简化，由于每行每列上均只能有一个棋子，我们只需要记录哪些行和列是已经拜访了棋子的，哪些是未摆放棋子的，同时需要记录目前为止，
每个已摆放棋子的行列坐标，对于每一个新棋子，我们要判断他将要放的位置行列是否空余，已经是否与之前已摆放的棋子在同一斜行上。
