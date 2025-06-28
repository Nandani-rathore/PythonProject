# # ---------------- question 1 -----------------
# import pandas as pd
# import re
# data = {
#     'email':['test@gmail.com','wrong_email.com','user123@yahoo.in'],
#     'mobile':['9828312345','9988776655','1234567890'],
#     'string':['hello123','nandinirathore','hello@123']
# }
#
# df = pd.DataFrame(data)
# # validate the email
# df['email_valid'] = df['email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0_9.-]+\.[a-zA-Z]{2,}$')
#
# # mobile validation for india (+91)
# df['mobile_validate'] = df['mobile'].str.match(r'^[6-9]\d{9}$')
#
# # string alphanumeric validate
# df['string_valid']=df['string'].str.match(r'[A-Za-z0-9]+$')
#
# print(df)
# print(df.to_string())


#--------------------------------------------- question2 -----------------------------------

#import pandas as pd
# data = {
#     'date':['18-07-2005','07-02-2007','23-11-2000']
# }
#
# df = pd.DataFrame(data)
# df['date']=pd.to_datetime(df['date'])
# print(df)
#
# df['year'] = df['date'].dt.year
# print("\nprint year:\n",df)
#
# df['month']=df['date'].dt.month
# print("\nprint the month:\n",df)
#
# df['day']=df['date'].dt.day
# print("\nprint the Day:\n",df)
#
# df['weekday']=df['date'].dt.day_name()
# print("\nprint the weekdays: \n",df)
#
#
# future = df[df['date'] > '2025-06-01']
# print("future dates :",future)


# ---------------------------- question3 ------------

import pandas as pd
df = pd.read_csv('people.csv')
print("\nprint first 5 rows:\n",df.head())

# data cleanup

print("missing values in each column:")
print(df.isnull().sum())

# if null value then drop it
cleaned_df = df.dropna()

# basic analysis

print("basic analysis:")
print(df.columns)
# show the count of males and female
gender_count = df['Sex'].value_counts()
print("Gender count:\n",gender_count)



# find uniques job title
uni= df['Job Title'].unique()
print("\nunique job titles :",uni)


#filter users with job title containing manager
# manager = df[df['job Title'].str.contains('Manager' , case=False , na =False)]
# print("\nmanager list:\n",manager[['First Name','job Title']])









































































