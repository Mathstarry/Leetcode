## 思路与想法
### 方法一：数学
**思路**：  
这也是单独一类的题型，如果暴力计算，则会超时。凭借 [offer43](https://github.com/Mathstarry/Leetcode/tree/master/getOffer/offer43_countDigitOne) 题的经验容易想到，可以打表观察规律。  

<img src="https://github.com/Mathstarry/Leetcode/blob/master/getOffer/offer44_findNthDigit/img/offer44_pic1.png" width = "500" height = "250" alt="" align=center />

因为题目限制 `0 <= n <= 2^31`，所以 `n` 大概在 2 * 10<sup>9</sup> 附近，动态数组只要开到长度 10 就肯定够用。观察到规律之后，让 `n` 依次与 [10<sup>i</sup>, 10<sup>i</sup> - 1] 比较，当 `n` 较小时，那 `n` 就在这个范围内了。此时若从 10<sup>i</sup> 开始枚举，依然会超时，但不难发现，这个区间内每个数字的长度是相同的，所以让 `n-1` 对这个区间长度取余即可，商表示 `n` 在这个区间的第几个数，余数表示 `n` 在这个数字的第几位。至于为什么用 `n-1`，这个举个例子就很容易想通了，留作思考。


**时间复杂度**：*O*(*1*)  
**空间复杂度**：*O*(*1*)
