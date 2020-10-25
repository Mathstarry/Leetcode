## 思路与想法
### 方法一：动态规划
**思路**：  
要将数组分割成和相等的两部分，等价于我们从数组中选中某几个元素，使得他们的和恰好为数组所有元素和的一半。所以一开始可以先处理两个特例，当数组所有元素之和为奇数，或者数组最大元素值大于数组元素之和
的一半时，此时不存在满足要求的序列。  
从数组中选取若干元素，即表明每个元素都只有被选取与不被选取两种情况。使得他们的和恰好为数组所有元素之和的一半，记为 V，等价于一个 0-1 背包问题，每件物品的价值和体积相等，且等于它的元素值，目标是
去若干件物品，使得他们的体积之和不超过 V 且价值为 V，每件物品最多只能被选取 1 次。


**时间复杂度**：*O*(*NV*)，其中 *N* 为数组的长度， *V* 为数组元素和的一半。   
**空间复杂度**：*O*(*NV*)