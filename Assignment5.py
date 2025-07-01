# # ---------------------------------- question1 ---------------------------------
# # create list from dictionary
# import pandas as pd
# data = {
#     "A":1,
#     "B":2,
#     "C":3,
#     "D":4
# }
#
# s = pd.Series(data)
# print(s)
#
#
# # create series from list
#
# listData = ["apple","mango","grapes","banana","orange"]
# sl = pd.Series(listData)
#
# print(sl)
#
#
# # Access the elements of the series
#
# print("access by label :",s['C'])
# print("access by index :",s[1])
# print("access by loc :",s.loc["B"])
# print("access by iloc :",s.iloc[1])
# print("access by slicing :\n",s[1:3])
import pandas as pd

## ------------------ question2 ---------------------
#
# import pandas as pd
#
# print("DataFrames from 2D Python List")
# data = [
#     [1,'Nandani Rathore','nandini@123','DS'],
#     [2,'Payal Mehta','payal@123','AI'],
#     [3,'Nitesh Mishra','nitesh@123','Civil'],
#     [4,'Seijal Jain','seijal@123','IT']
# ]
#
# df = pd.DataFrame(data,columns=['id','Name','email_id','Branch'])
# print(df)
#
#
# print("dataframes from dictionary")
# dataDict = {
#     'count':[1,2,3,4,5,6],
#     'Alphabat':['a','b','c','d','e','f'],
#     'fruits' :['apple','mango','grapes','banana','orange','chickoo']
# }
#
# print()
# s1 = pd.DataFrame(dataDict)
# print(s1)
#
#
# print("Pandas dataframes from list of tuples")
# datatuple = [(1,2,3),
#              ('One','Two','Three'),
#              (4,5,6)
#              ]
#
# st = pd.DataFrame(datatuple)
# print(st)
#
#
#
# print("Pandas dataframes from list of dictionary")
# datald = [
#     {'A':'apple'},
#     {'B':'boy'},
#     {'C':'cat'},
#     {'D':'dog'}
# ]
#
# sld = pd.DataFrame(datald)
# print(sld)



# --------------------------- question 3 -------------------------

# 1. differwnt ways to iterate

import pandas as pd
data1 = {
   'name':['payal','Ekta','Rahul','Mayank'],
    'age':[12,14,15,18],
    'city':['Delhi','Mumbai','Agra','kota']
}

df = pd.DataFrame(data1)
print(df)

print("using iterrow()")
for index,row in df.iterrows():
    print(f"name : {row['name']}, age:{row['age']}")

print("using itertuple()")
for row in df.itertuples():
    print(f"name:{row.name}, city:{row.city}")

# 2.selecting any row based on condition

print("selecting any row based on condition ")
result = df[df['city']=='Delhi']
print(result)


# 3. select row using iloc[]

print()
print("select row using iloc[]")
res = df.iloc[2]
print(res)

#  4. limited row selection with given column

print()
print("limited row selection with given column ")
r = df.loc[0:2,'city']
print(r)


# 5. Drop row based on condition

print()
print("Drop row based on condition")
rem = df[df['age'] != 14]
print(rem)

# 6. insert row at given position

print()
print("insert row at given position")
newData = {'name':'kavya','city':'jaipur','age':19}
df1 = pd.concat([df.iloc[:2],pd.DataFrame([newData]),df.iloc[2:]]).reset_index(drop=True)
print(df1)

# 7. create a list from rows in DataFrames

print()
print("create a list from rows in DataFrames")

l = df.to_dict(orient='records')
print(l)


























































































































































