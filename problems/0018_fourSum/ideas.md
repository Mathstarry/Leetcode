## 思路与想法
### 方法一：四指针
**思路**：  
为了防止重复，先要对数组进行排序。然后用双指针和双循环遍历数组的前 n-2 个元素，接下来再用双指针从剩余数组的两端开始向中间搜索，判读四个指针指向的数字之和是否满足条件。
我们可以加入剪枝操作，判断四数之和明显小于目标值或者明显大于目标值时，进行剪枝，放弃该段循环。


**时间复杂度**：*O*(*N*<sup>3</sup>)  
**空间复杂度**：*O*(*N*)