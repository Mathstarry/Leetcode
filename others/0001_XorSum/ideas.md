## 思路与想法
### 方法一：单调栈
**思路**：  
数据的范围是 `[1, 1e6]`，子区间总共有 `n + (n-1) + ··· + 1 = n(n+1)/2` 个，如果枚举每一个区间，并寻找其最大最小值(每个区间是 O(*l*) 的搜索时间，*l* 为区间长度)，必然会导致超时。  
但是数据总共只有 `n` 个，所以可以枚举每一个值，并计算他们作为最大最小值时，所影响的区间个数，这样就可以以 O(*N*) 的时间解决问题。解决本问题有以下几个要点：  
1. 结果是所有区间的最大最小值的异或，而异或操作具有可交换性，也就是说先把所有的最小值取异或，再与所有的最大值取异或，并不影响结果，所以我们可以分别找出所有最小值和最大值，而不需要捆绑地寻找。
2. 可以枚举每一个值作为最小值时所影响的区间范围，该范围的大小可由单调递增栈 O(*N*) 地得到，同理，枚举每个值作为最大值时，可以用单调递减栈得到。
3. 在得到某个值作为最值的区间范围后，用该点**左边的区间长度**乘以该点**右边的区间长度**，就可以得到**包含该点**且**以该点为最值**的所有子区间数量。
4. 相同的值进行异或之后结果为 0，进而可以得到，偶数个相同值进行异或结果为 0，奇数个相同值异或结果与单个值相同。
5. 得到每个值作为最值出现在的子区间数量对 2 取余，再把所有取余结果为 1 的值进行异或操作，就可以得到题目所求的结果了。

**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)
