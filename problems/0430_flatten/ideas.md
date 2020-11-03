## 思路与想法
### 方法一：递归
**思路**：  
对于每一个节点，如果它的后继节点和孩子节点均为空，则终止递归。若其存在后继节点，但孩子节点为空，则递归其后继节点。若其存在孩子节点，后继节点为空，则将其孩子节点更改为其后继节点，并更改相应的前置节点，
然后递归其原来但孩子节点。若某个节点同时存在后继节点与孩子节点，则先存下其后继节点的索引，然后将其孩子节点更改为其后继节点，并递归其原来的孩子节点，递归返回到此处时，将之前存下的后继节点更改成递归
所返回的节点的后继节点。


**时间复杂度**：*O*(*N*)  
**空间复杂度**：*O*(*N*)