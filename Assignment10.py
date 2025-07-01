from math import isnan

import numpy as np

arr = np.array([[6,-8,73,-110],[np.nan,-8,0,94]])
res = np.nan_to_num(arr,nan=0)
print("\nThe Original Array is:\n",arr)
print("\nArray after replacement is:\n",res)

print("\nArray after replacing 3 rows and column:\n")
arr[[1,2,3],:] = arr[[3,2,1],:]
print(arr)


# --------------------------- question2 ------------------------------

arr_3d = np.array([ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\nThe Original array is:\n",arr_3d)

new = np.moveaxis(arr_3d,0,1)
print("\nArray after axes movement is :\n",new)

# ---------------------------- question3 -----------------------------

arr = np.array([[12,13,np.nan,43],[43,56,65,np.nan],[12,np.nan,np.nan,11]])
print("\nThe Original array is:\n",arr)

avg = np.nanmean(arr,axis=0)
print(avg)

indices = np.where(np.isnan(arr))

arr[indices] = np.take(avg,indices[1])
print("\nThe new array is:\n",arr)


# ----------------------- question 4 ----------------------

arr = np.array([[12,-15,2,3,4,-77,4],[11,22,-2,43,2,-2,-4],[9,8,-4,-5,-6,-7,6]])
print("\nThe array is :\n",arr)

# print(arr<0)
arr[arr<0] = 0
print("\nThe new array after replacement is:\n",arr)



# -------------------- question 5,6,7 --------------------

import numpy as np
arr1 = np.array([[3,4],[1,2]])
arr2 = np.array([[1,0],[3,4]])
avg =  (arr1+arr2)/2
print("Array 1 is:\n",arr1)
print("Array 2 is:\n",arr2)
print("\nThe average of arr1 and arr2 is:\n",avg)

combine = np.vstack((arr1,arr2))
mean = np.mean(combine)
print("\nMean is:\n",mean)

median = np.median(combine)
print("The Median is:\n",median)



# ---------------- question 8 ----------------

import numpy as np
a = np.array([[1,-2,3],[-1,3,-1],[2,-5,5]])
b = [9,-6,17]

result = np.linalg.solve(a,b)

print("Value of x is:",result[0])
print("Value of y is:",result[1])
print("Value of z is:",result[2])



# ----------------------- question 9 ---------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

semester =np.array(['1st','2nd','3rd','4th','5th','6th','7th','8th'])
cgpa = np.array([7,7.5,9,9.5,9.7,6,9.84,4])

plt.plot(semester,cgpa,color='blue',linestyle='--',marker='o')
plt.title("Semester wise cgpa comparision(line plot)")
plt.xlabel("semester")
plt.ylabel("CGPA")
plt.show()


plt.bar(semester,cgpa,color='orange')
plt.title("Semester wise cgpa comparision(Bar Graph)")
plt.xlabel("semester")
plt.ylabel("CGPA")
plt.show()


plt.scatter(semester,cgpa,color='blue')
plt.title("Semester wise cgpa comparision(Scattered Graph)")
plt.xlabel("semester")
plt.ylabel("CGPA")
plt.show()



plt.hist(cgpa,bins=30)
plt.title("Semester wise cgpa comparision(Histrogram)")
plt.xlabel("semester")
plt.ylabel("CGPA")
plt.show()


plt.pie(cgpa,labels=cgpa,autopct='%1.1f%%')
plt.title("Semester wise cgpa comparision(pie chart)")
plt.xlabel("semester")
plt.ylabel("CGPA")
plt.show()








































