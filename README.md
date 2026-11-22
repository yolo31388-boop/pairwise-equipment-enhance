# pairwise-equipment-enhance

## 领域

游戏、图形与多媒体

## 主题

装备强化

## 说明

服务端概率、保底与并发锁。

初始状态下 `gameplay/equipment_enhance.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
