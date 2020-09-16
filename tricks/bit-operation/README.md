# 位运算技巧

## 亦或运算 `^`

1. 当 `x` 为奇数时， `x` 的二进制表示的末位为 `1`，所以我们有 `x ^ 1 = x - 1`；  
   当 `x` 为偶数时， `x` 的二进制表示的末位为 `0`，所以我们有 `x ^ 1 = x + 1`。
   
   应用见 765minSwapsCouples 情侣牵手
   