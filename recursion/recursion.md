# 递归
- 什么是递归？
- 如图：![](https://pic2.zhimg.com/80/22cc736d26514b650b7bd25408f48011_hd.jpg)

***递归要有一个终点（小鲤鱼）
当递归尚未达到终点的时候，函数会反复调用自己。***

#### 示例：
要在一堆盒子中找到一个钥匙的递归伪代码：
```python
def look_for_key(box):
    for item in box:
        if item.is_a_box:
        	look_for_key(item)
        else:
        	print('find a key')
```    

> 编写递归函数时,必须告诉它何时停止递归。正因为如此,每个递归函数都有两部分:基线
条件(base case)和递归条件(recursive case)。递归条件指的是函数调用自己,而基线条件则
指的是函数不再调用自己,从而避免形成无限循环。