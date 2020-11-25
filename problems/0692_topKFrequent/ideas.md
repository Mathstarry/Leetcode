## 思路与想法
### 方法一：堆
**思路**：  
先用一个字典记录每个单词出现的频率，然后把 (-频率, 单词) 对存入堆中，接着 pop 出小顶堆中的前 k 个单词即可。


**时间复杂度**：*O*(*N log k*)  
**空间复杂度**：*O*(*N*)