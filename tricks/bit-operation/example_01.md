## 例一

考虑如下一个状态压缩问题，把 9 个变量，共 2<sup>9</sup> 种状态，压缩到一个长度为 9 的二进制数中，也就是一个范围为 [0, 2<sup>9</sup>) 的整数中。  
假设变量 A，B，C 均在上述范围内，对于数字 k 属于 [1, 9]，当且仅当它均不在 A，B，C 中时，我们才能把它加入 A，B，C 中的一个。  
那么我们有 '~(A | B | C) & 2<sup>9</sup> - 1`表示 A，B，C 中所有满足条件的位置 k，我们可以回溯地尝试这些位置。  
相关题目见 [37. 解数独 方法二]()
