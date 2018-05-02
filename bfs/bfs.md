# 广度优先搜索
*主要内容*
- 用图来建立网络模型
- 学习广度优先搜索
- 学习有向图和无向图
- 学习拓补排序

### 图简介
图模拟一组连接。例如,假设你与朋友玩牌,并要模拟谁欠
谁钱,可像下面这样指出Alex欠Rama钱。
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/bfs/1.png)
完整的欠钱图可能类似于下面这样
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/bfs/2.png)
- 图由节点(node)和边(edge)组成
- 一个节点可能与众多节点直接相连,这些节点被称为**邻居**
- 图用于模拟不同的东西是如何相连的
* python中实现图结构：
```python
lan = {}
lan['me'] = ['chao','xiang','233']
```
将字典中的键映射到一个数组，该键包含了所有邻居结点
- 有向图，有指向自己的结点，自己不指向别人
- 无向图，没有箭头，直接相连的结点互为邻居
### 广度优先搜索
*广度优先搜索是一种用于图的查找算法*
可帮助解决两类问题
- 1.从A结点出发，是否有前往结点B的路径
- 2.解决最短路径问题  

**在广度优先搜索的执行过程中,搜索范围从起点开始逐渐向外延伸,即先检查一度关系,再检查
二度关系**  

`添加顺序进行检查`——>>> **队列**：		
队列是一种先进先出（*First in First Out*）的数据结构,  
而栈是后进先出（*Last in First out*）
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/bfs/3.png)
#### [实现算法(bfs.py)](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/bfs/bfs.py)
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/bfs/4.png)