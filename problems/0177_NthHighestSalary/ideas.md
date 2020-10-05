## 思路与想法
### 关键词：`GROUP BY`, `LIMIT OFFSET`, `SET`
**思路**：  
找到第 N 高的薪水思路与找到第二高的薪水是一样的，需要注意的是，使用 `limit N, 1` 与 `limit 1, offset N` 是合法的，而使用 `limit N-1, 1` 与 `limit 1, offset N-1` 是非法的。
所以在 `BEGIN` 与 `RETURN` 之间，要加上 `SET N = N - 1`，这样才能返回第 N 高第薪水。具有去重作用的指令除了 `DISTINCT` 之外还有 `GROUP BY`。

