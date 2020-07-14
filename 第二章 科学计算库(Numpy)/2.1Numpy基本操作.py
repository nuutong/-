import numpy as np
array = np.array([1,2,3,4,5])
print(type(array))

array2 = array + 1
print(array2)

print(array2 + array)
print(array * array2)

print(array.shape)

#python中list结构没有shape属性
#tang_list=[1,2,3,4,5]
#print(tang_list.shape)

#二维数组
print(np.array([[1,2,3],[4,5,6]]))

#ndarray中所有元素必须是同一类型，否则自动向下转换，int->float->str
tang_list=[1,2,3,4,'5']
tang_array=np.array(tang_list)
print(tang_array)
tang_list=[1,2,3,4,5.0]
tang_array=np.array(tang_list)
print(tang_array)

#打印当前数据格式
print(type(tang_array))
#打印当前数据类型
print(tang_array.dtype)
#打印当前数组中元素个数
print(tang_array.size)
#打印当前数据维度
print(tang_array.ndim)