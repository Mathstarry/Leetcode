## 思路与想法
### 方法一：计数
**思路**：  
本题只需要考虑有车停进来的情形，不需要考虑有车开走的情形，所以一开始写好大中小车位的容量，有车停进相应车位，如果车位没满，车位容量就减一并返回 `True`，否则返回 `False`。
