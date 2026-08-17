import numpy as np

print("\n-----------------     Array 1-D   -----------------")

ar=np.zeros(6)
print(ar)
ar=np.ones(6)
print(ar)
ar=np.full(6,2)
print(ar)

ar=np.arange(1,12,2)
print(ar)

random_num=np.random.randint(1,6)
print(" random_num int: ",random_num)

random_num_otp=np.random.randint(1000,9999,6)
print(" random_num_ otp int: ",random_num_otp)

random_num = np.random.rand(5)
print("random_num -5: ",random_num)

random_num=np.random.random(6)
print("random_num :",random_num)

print("\n-----------------     Array    -----------------")
arr1d=np.array([10,20,30,45,65,85])


print("\n-----------------     Array 1-D   -----------------")
print(arr1d)
"""
arr1d.reshape(3,2)
print(arr1d)
"""

print("\n----------------     Array 2-D     ----------------------")
arr2d=np.array([
    [10,20],
    [30,65]
])



print("\n----------------      Array Properties     -----------------------")
print(arr2d)
print(arr2d.ndim)
print(arr2d.shape)
print(arr2d.size)
print(arr2d.dtype)

newArr=arr2d.reshape(1,4)
print("reshape : ",newArr)

print("\n-----------------          Flatten Array   ------------------------")
arrFlat=arr2d.flatten()
print(arrFlat)

print("\n---------------------------------------------")


arr3d=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ],
[
        [9,10],
        [11,12]
    ]
])

print("\n===================  Array 3-d ====================")
print("arr3d :: ",arr3d,"\nsize :: ",arr3d.size,"\nndim :: ",arr3d.ndim,"\nshape :: ",arr3d.shape)
print("arr3d[0][1][1] value is ::",arr3d[0][1][1])

print("\narr3d[2][1][2] value is ::",arr3d[2][1][1])

print("\n===================  ====================")
a= np.array([1,2,3,4,5])
b=np.array([10,20,30,40,50])

print("\n-------------------   Add using 2 Array   --------------------------")
c=a+b
print(c)

print(a+100)
print(a*100)


print("\n-----------------    STATISTICAL OPERATIONS    ---------------------")

stats_num=np.array([12,24,36,45,85,96])

print("\nmax ",stats_num.max(),"\nmin ::",stats_num.min())

print("\n-----------------   MORE STATISTICAL OPERATIONS    ---------------------")
classA = np.array([48, 49, 50, 51, 52]) # mean is 50
classB = np.array([20, 40, 50, 60, 80]) # mean is 50

mean_average=classA.mean()
print("mean_average : ",mean_average)

median_classA=np.median(classA)
print("median_classA :: ",median_classA)
"""
stdVal=np.std(classA,classB)  # use or to verify data quality if mean is same
print("stdVal : ",stdVal)

variants_data=np.var(classA,classB)
print("variants_data : ",variants_data)
"""

p1_stock_returns = [10, 11, 9, 10, 10]
p2_stock_returns = [2, 20, -5, 25, 8]
print("  ==========  MEAN ================ ")
print(np.mean(p1_stock_returns))
print(np.mean(p2_stock_returns))

print("  ==========  np.std(a,b) ================ ")
print(np.std(p1_stock_returns))
print(np.std(p2_stock_returns))

print("  ==========  np.var(a,b) ================ ")
print(np.var(p1_stock_returns))
print(np.var(p2_stock_returns))

print("  ==========  boolean condition and sorting ================ ")

a = np.array([98,45,86,20,89])
sorted=np.sort(a)
print("sorted : ",sorted)

a=a[a>60]
print(a)

arr = np.array([1, 2, 3, 4, 5, 6])
even_numbers = arr[arr % 2 == 0]
print(even_numbers)

arr = np.array([1, 2, 3, 4, 5, 6])
odd_numbers = arr[arr % 2 == 1]
print(odd_numbers)

print(" ******************   Copy Example ***********************")

arr1 = np.array([10, 20, 30])
arr2 = arr1.copy()
arr2[0] = 100
print(arr1)
print(arr2)

print(" ******************    View Example *********************** ")
arr1 = np.array([10, 20, 30])
arr3=arr1.view()
arr3[0] = 100
print(arr1)
print(arr3)