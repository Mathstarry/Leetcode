# 树状数组
在树状数组中，数组是名词，树是定语，所以本质上还是一个数组，但是我们把数组排列成了树形结构。  
不妨考虑一个长度为 `n` 的数组，数组的特性是可以通过索引 O(1) 地访问每一个元素的值，但是如果想要求前 `i` 项和，就需要 O(*N*) 的时间，为了更快地得到前 `i` 项和，考虑另外用一个长度为 `n` 的数组
记录原数组的前 `i` 项和，称之为前缀和数组，这样就可以 O(*1*) 地得到原数组的前 `i` 项和，但是每当原数组中的某一个值改变时，我们就需要 O(*N*) 地去改变前缀和数组的前 `i` 项的值。

为了更快地访问和更新原数组的前 `i` 项和信息，提出了树状数组的概念，如下图所示：





## 树状数组题目

### 简单


---
### 中等


---
### 困难
[offer51. 数组中的逆序对](https://github.com/Mathstarry/Leetcode/tree/master/getOffer/offer51_reversePairs)