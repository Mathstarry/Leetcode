### 思路
**方法一：回溯法**  
建立三个字典数组 `rows`， `cols`， `boxs` 分别用来表示某一行、某一列、某一三宫格内是否存在数字 `t`。
声明全局变量 `self.solved`，如数独未被解出，则在回溯时需要将已填的数字变回 `'.'`，如已解出，则直接返回。这样便可原地修改九宫格了。  
[**代码**](https://github.com/Mathstarry/Leetcode/blob/master/problems/0037_solveSudoku/solution1.py)

**方法二：状态压缩**  
本方法参考自力[扣官方题解方法二](https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode-solution/)。  
想法仍同上，用回溯来寻找唯一解，但是不再用字典数组存储状态，而是把数字 1～9 是否存在压缩到一个范围在 [0, 2<sup>9</sup> - 1] 之间的整数，并用三个数组分别存储行、列、块信息。
具体算法实现上会用到许多[位运算的技巧](https://github.com/Mathstarry/Leetcode/blob/master/tricks/bit-operation/README.md)。
本方法的时间复杂度仍同方法一，但是由于进行了状态压缩，所以速度会略微快一点。在力扣上由方法一的176ms加快到了140ms。  
[**代码**](https://github.com/Mathstarry/Leetcode/blob/master/problems/0037_solveSudoku/solution2-bitmask.py)
