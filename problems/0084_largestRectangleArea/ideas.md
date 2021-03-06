## 思路与想法
### 方法一：单调栈
**思路**：  
单调栈与单调队列有时不会严格区分，因为使用时既会从队首出列，也会从队尾出列。本题要求最大矩形面积，显然一个矩形只有存在与其相邻且高度比他高的矩形时，宽度才可以增加，利用这一点可以使用单调栈。
所以，当某一高度的一系列矩形两侧的高度都低于它时，就可以计算该高度构成的最大面积。
基本思路：  
维护一个单调非减的栈，若当前矩形高度不小于栈尾矩形的高度，则入栈；否则，从队尾一直出栈，直到队尾矩形的高度不大于当前矩形高度为止，且对于每一个出栈的矩形，此时可以计算以它为高的矩形的最大面积。
对于每一个出栈的矩形，不妨设其高度为 `h`，栈外当前矩形索引为 `j`，栈尾倒数第二个矩形的索引为 `i`，此时更新最大面积 `res = max(res, h*(i-j-1))`，因为对于栈中的每一个矩形而言，它左边的
第一个矩形一定是第一个不高于它的矩形，而栈外的当前矩形又是它右边第一个低于它的矩形，因此以栈尾矩形为高的矩形面积可以计算。但需要注意的是，当栈尾有多于一个高度为 `h` 的矩形时，需要计算到最左侧的
高度为 `h` 的矩形时，才是以 `h` 为高的最大矩形面积。

**时间复杂度**：*O*(*n*)  
**空间复杂度**：*O*(*n*)
