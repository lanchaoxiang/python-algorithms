# 散列表（字典）
*学习散列表的内部机制:实现、冲突和散列函数。理解如何分析散列表的性能*


- 散列函数：  “将输入映射到数字”
- Python提供的散列表实现为字典,你可使用函数 dict 来创建散列表

```python
book ={}
book['a'] = 1
book['b'] = 2
book['c'] = 3
>>>print (book)
{'a':1,'b':2,'c':3}
```
- 散列表由键和值组成,散列表将键映射到值  
>例如：DNS解析


- 防止重复
- 将散列表用作缓存（网站将数据记住，而不重新计算）

*缓存是一种常用的加速方式,所有大型网站都使用缓存,而缓存的数据则存储在散列表中!*   
  
  
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/hash_table/1.png)
![](https://raw.githubusercontent.com/lanchaoxiang/python-algorithms/master/hash_table/2.png)  
``` python  
cache = {}
def get_page(url):
	if cache.get(url):
    	return cache[url]
    else:
    	data = get_data_from_server(url)
        cache [url] = data
        return data
```

##### 小结
散列表用于：

 模拟映射关系;  
 防止重复;  
 缓存/记住数据,以免服务器再通过处理来生成它们。

### 散列表冲突

两个键映射到了同一个位置称为散列表冲突  
*解决方法*：
在该位置存储一个链表  

*这里的经验教训有两个*
- 散列函数很重要。前面的散列函数将所有的键都映射到一个位置,而最理想的情况是,
散列函数将键均匀地映射到散列表的不同位置  
- 如果散列表存储的链表很长,散列表的速度将急剧下降。然而,如果使用的散列函数很
好,这些链表就不会很长!

### 散列表性能
*避免冲突*
- 较低的填装因子： 填装因子 = 散列表包含的元素数/位置总数 >> 度量的是散列表中有多少位置是空的 
> 填装因子越低,发生冲突的可能性越小  
> 一旦填装因子超过0.7,就该调整散列表的长度


-  良好的散列函数(SHA函数)
> 良好的散列函数让数组中的值呈均匀分布
> 糟糕的散列函数让值扎堆,导致大量的冲突



