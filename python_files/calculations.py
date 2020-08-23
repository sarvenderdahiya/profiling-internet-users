import pandas as pd
from os import listdir
from scipy.stats import spearmanr

wind10sec_path = '../processed_files/10sec_file/'
wind227sec_path = '../processed_files/227sec_file/'
wind300sec_path = '../processed_files/300sec_file/'
postprocess_folder = '../postprocessed_files/'

path_list = [wind10sec_path, wind227sec_path, wind300sec_path]

def perform_calc():

    # for each path of the processed files (10sec , 227sec etc)
    ind = 0
    windname = ['10', '227', '300']

    # pass files to calculate function:
    for path in path_list:
        file_list = [f for f in listdir(path) if not (f.startswith('.') or f.startswith('~'))]
        calculate(path, file_list[0], windname[ind])
        ind += 1



def calculate(path, filename, windname):
    filepath = path + filename
    df = pd.read_csv(filepath)

    # split dataframes by weeks
    df_week1 = df[df.week == 'Week1']
    df_week2 = df[df.week == 'Week2']
    df_week1.drop(['window_start', 'week'], axis=1, inplace=True)
    df_week2.drop(['window_start', 'week'], axis=1, inplace=True)
    header_list = [i for i in range(54)]
    df = pd.DataFrame(columns=header_list)
    df1 = pd.DataFrame(columns=header_list)
    df2 = pd.DataFrame(columns=header_list)
    #print(header_list)
    print(df.info())

    print(df_week2.shape[1], '****')

    # Create a dataframe which contains the spearman coefficients
    # it passes every user from week 1, and calculates spearman coefficient against every
    # other user in week 2. Saves that to a list and appends the corresponding user's lists
    # to the dataframe
    for i in range(df_week1.shape[1]):
        somelist = []
        somelist1 = []
        somelist2 = []

        for j in range(df_week2.shape[1]):
            rho, p = spearmanr(df_week1.iloc[:,i],df_week2.iloc[:,i] )
            rho1, p1 = spearmanr(df_week1.iloc[:,i], df_week2.iloc[:,j])
            rho2, p1 = spearmanr(df_week2.iloc[:,i], df_week2.iloc[:,j])
            somelist.append(rho)
            somelist1.append(rho1)
            somelist2.append(rho2)

        someseries = pd.Series(somelist, index=df.columns)
        someseries1 = pd.Series(somelist1, index=df1.columns)
        someseries2 = pd.Series(somelist2, index=df2.columns)

        df = df.append(someseries, ignore_index=True)
        df1 = df1.append(someseries1, ignore_index=True)
        df2 = df2.append(someseries2, ignore_index=True)

        #print(df.shape[0], " appended ")

    #print(df.info())
    df.fillna(0.001, inplace=True)
    df1.fillna(0.001, inplace=True)
    df2.fillna(0.001, inplace=True)

    outputpath = postprocess_folder + windname +"r1a2a.csv"
    outputpath1 = postprocess_folder + windname + "r1a2b.csv"
    outputpath2 = postprocess_folder + windname + "r2a2b.csv"

    df.to_csv(outputpath)
    df1.to_csv(outputpath1)
    df2.to_csv(outputpath2)





