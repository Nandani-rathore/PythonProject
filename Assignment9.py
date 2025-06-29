# ---------------------------- question1 -------------------------------
import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_1d.shape)
arr_1d = arr_1d.reshape(1,3)

print("\n1D array is:\n",arr_1d)
print("\n2D array is:\n",arr_2d)
result = np.concatenate([arr_1d,arr_2d],axis=0)
print("\nMerging of array is :\n",result)

# at axis 1

# x = arr_1d.reshape(2,-1)
# res = np.concatenate([x,arr_2d],axis=1)
# print("concatination along y axis:\n",res)


# --------------- question2 ---------------

arr_2d = np.array([[1,2,3],[5,6,7],[8,9,10]])
print("\n Flattining of 2d array is :\n")
result = arr_2d.reshape(-1)
print(result)


# ------------------------ question3 ---------------------

arr1 = np.array([9,8,7,6,5,4,3])
rev_arr = arr1[::-1]
print("\nThe original array is:\n",arr1)
print("\nThe Reverse array is :\n",rev_arr)


# -------------------- question4 --------------

arr1 = np.array([ [[12,32,45],[12,4,5]],[[11,33,54],[435,56,432]],[[34,564,523],[334,5,6]]])
print("The array is the:\n",arr1)
print("the shape of the array is:\n",arr1.shape)

min_el = arr1.min()
print("\nThe Minimum element in the array is:",min_el)

max_el =arr1.max()
print("The Maximum element in the array is:",max_el)

block,rows,cols = arr1.shape
print("\nNo. of blocks:",block)
print("No of Rows:",rows)
print("No of columns:",cols)

print("\nselect all the elements of teh array :")

for block in arr1:
    for row in block:
        for x in row:
            print(x,end="  ")


print("\nprint specific element: 1 block,2 row , 3 element:")
print(arr1[0,1,2])


print("\nSum of 2d array is:")
s = arr1.sum()
print(s)
print("\nAxis 0 sum is:\n",np.sum(arr1,axis=0))
print("\nAxis 1 sum is:\n",np.sum(arr1,axis=1))

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[11,22,33],[44,55,66]])

print("\nAddition of 2 Numpy array is:\n",a+b)
print("\nSubtraction of 2 Numpy array is:\n",a-b)
print("\nMultiplication of 2 Numpy array is:\n",a*b)
print("\nDivision of 2 Numpy array is:\n",a/b)



















