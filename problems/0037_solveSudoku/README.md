# 37. [解数独](https://leetcode-cn.com/problems/sudoku-solver/)  
<font size=5> 难度 `困难` </font>
---

### 题目描述

编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需**遵循如下规则**：

  1. 数字 `1-9` 在每一行只能出现一次。
  2. 数字 `1-9` 在每一列只能出现一次。
  3. 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。
空白格用 `'.'` 表示。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0037_solveSudoku/img/Sudoku1.png" width = "270" height = "270" alt="" align=center />

一个数独。

<img src="https://github.com/Mathstarry/Leetcode/blob/master/problems/0037_solveSudoku/img/Sudoku2.png" width = "270" height = "270" alt="" align=center />

答案被标成灰色。

Note:

* 给定的数独序列只包含数字 `1-9` 和字符 `'.'` 。
* 你可以假设给定的数独只有唯一解。
* 给定数独永远是 `9x9` 形式的。

### 题解
**方法一**：
回溯法，建立三个字典 `rows`， `cols`， `boxs` 分别用来表示某一行、某一列、某一三宫格内是否存在数字 `t`。
声明全局变量 `self.solved`，如数独未被解出，则在回溯时需要将已填的数字变回 `'.'`，如已解出，则直接返回。这样便可原地修改九宫格了。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
