## 思路与想法
### 方法一：哈希表
**思路**：  
首先需要用一个哈希表来记录每个单词中都出现的字母出现的最小频率，具体操作是，先建立频率字典，默认值设为 -1，然后对数组中的每一个单词，统计其中每个字母出现的频率，再去更新频率字典中每个字母出现的频率即可。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)