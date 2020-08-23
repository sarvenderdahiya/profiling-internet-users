
# ******************************************
# This File is just to Test Some pieces of code
# It has no significance to the Project
# ******************************************


# import pandas as pd
#
# df = pd.read_csv('../10sec_file/all_user_10sec.csv')
# print(df.info())
#
# df_week1 = df[df.week == 'Week1']
# print (df_week1.info())

# ******************************************

# from datetime import datetime
#
# realfirstpkt = 1361566800.002
# time = datetime.fromtimestamp(realfirstpkt)
#
# print(time)
# print (time.time())
# for i in range(1,3):
#     print(i)


# *****************************************


# import pandas as pd
#
# original_filepath = '../original_files'
# df = pd.read_excel('../original_files/ajdqnf.xlsx')
# list = df['Real First Packet']
# print(df.info())
# list = list.tolist()
#
# list1 = list
# list1.sort()
# print(list1 == list )
# for i in range(len(list)):
#     if ( list [i] != list1[i]):
#         print ( i)


# *****************************************

#
# import pandas as pd
# import numpy as np
#
# df = pd.DataFrame(np.arange(12).reshape(3, 4),
#                   columns=['A', 'B', 'C', 'D'])
# ind = 2
# rpckt = df._get_value(ind, 'B')
# print(df.head())
# print(rpckt)
# df = df.iloc[0:0]
# df = pd.DataFrame()
# print(df.head())


# *******************************************

# import pandas as pd
#
# l = [1,2,3,4]
# ll = [12.3, 12.3, 22.3, 44.2]
# # m = [21,25,3,14]
# # mm = [122.3, 1123, 22113, 44.2]
# lll = ['week1', 'week1', 'week1', 'week2']
# lllname = 'cc'
# df1 = pd.DataFrame({'aa':l, 'bb': ll})
# # df2 = pd.DataFrame({'aa':m, 'bb': mm})
# df1[lllname] = lll
#
# print(df1.iloc[:,1])


# *******************************************
# Code used to Fix the preprocessed file names which were saved as .xlsx instead of .csv
# But is not needed as The base code is fixed to make that change by default
# fix_filepath = "../preprocessed_files"
# to_fix = [f for f in listdir(fix_filepath) if not (f.startswith('.') or f.startswith('~'))]
# print (to_fix)
# for file in to_fix:
#     file_path = fix_filepath + "/" + file
#     print(file_path)
#     new_name = file_path.replace("xlsx","") + "csv"
#     print(new_name)
#     rename(file_path, new_name)

#************************************************
