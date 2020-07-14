import numpy as np

#数值索引
tang_array=np.array([1,2,3,4,5])
#[1:3]表示左闭右开，索引从0开始
print(tang_array[1:3])
#[-2:]表示从数组中倒数第二个数据开始取到最后
print(tang_array[-2:])

tang_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
tang_array[1,1] = 10
print(tang_array)

#取第二行数据
print(tang_array[1])
#取第二列数据(:相当于全部，即取某列的全部数据）
print(tang_array[:,1])


#bool索引
#从0开始到100，每隔10个数取一个元素
tang_array = np.arange(0,100,10)
print(tang_array)
#创建布尔类型的数组
mask = np.array([0,0,0,1,1,1,0,0,1,1],dtype=bool)
print(mask)
#通过布尔类型的索引选择元素
print(tang_array[mask])

#在[0,1)区间随机选择10个数
random_array=np.random.rand(10)
print(random_array)
#判断其中每个元素是否满足要求，返回布尔类型
mask = random_array > 0.5
print(mask)

tang_array = np.array([10,20,30,40,50])
#找到符合要求的索引位置
print(np.where(tang_array>30))
#按照满足要求的索引来选择元素
print(tang_array[np.where(tang_array>30)])

#数组对比
y = np.array([1,1,1,4])
x = np.array([1,1,1,2])
print(x == y)

print(np.logical_and(x,y))
print(np.logical_or(x,y))