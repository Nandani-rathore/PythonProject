# ----------------- question1 ---------------
#
# import pandas as pd
# data = ['18-07-2005','25-02-2006','07-02-2007','23-11-2000']
# date_series = pd.to_datetime(data)
# print("printing date Series is :",date_series)
#
# ts = pd.Series([10,20,30,40],index=date_series)
# print("\n time series is :\n",ts)
import pandas as pd

# ------------------------ question2 -----------------

#
# data1 = {
#     'name':['akon','bkon','ckon','dkon','ekon'],
#     'id':[1,2,3,4,5],
#     'age':[10,12,14,16,11]
# }
# df1 = pd.DataFrame(data1)
#
# data2 = {
#     'school_name':['pkon','dkon','fkon','hkon','mkon'],
#     'id':[6,1,3,4,9],
#     'sub':['maths','hindi','english','science','sst']
# }
# df2 = pd.DataFrame(data2)
# print(df1)
# print("\n\n",df2)
#
# # inner merge
#
# mer = pd.merge(df1,df2,on='id',how='inner')
# print("\nInner merge is :\n",mer)
#
#
# # left join
#
# ljoin = pd.merge(df1,df2,on='id',how='left')
# print("\nLeft join is :\n",ljoin)
#
# # index based join
#
# rmerge = pd.merge(df1,df2,on='id',how='right')
# print("\nRight join:\n",rmerge)
#
# df1.set_index('id',inplace=True)
# df2.set_index('id',inplace=True)
#
# indexJoin = df1.join(df2,how='right')
# print("\nIndex-based join is :\n",indexJoin)



# ------------------------ question 3 ----------------

df1  = pd.DataFrame({'id':[1,2,3],'name':['akon1','akon2','akon3']})
df2 = pd.DataFrame({'id':[4,5,6],'name':['bkon1','bkon2','bkon3']})
df3 = pd.DataFrame({'id':[2,3,4,5],'newName':['dkon','ekon','fkon','gkon']})

concat12 = pd.concat([df1,df2],axis=0)
print("\nAfter concatination:\n",concat12)

print("\ndf3:\n",df3)
finalConcat = pd.merge(concat12,df3,on='id',how='inner')
print("\nFinal Result is :\n",finalConcat)


















