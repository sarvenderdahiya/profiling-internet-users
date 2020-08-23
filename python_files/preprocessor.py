import pandas as pd

original_filepath = '../original_files/'
preprocessed_filepath = '../preprocessed_files/'
Mon4feb8am = 1359982800  # Timestamp on Monday Feb 4 8:00:00 am Local Time zone
Fri15feb5pm = 1360965600  # Timestamp on Friday Feb 15 5:00:00 pm Local Time zone


def preprocess(filename):

    filepath = original_filepath + filename

    # only read [Octets, Real First Packet, Duration] columns from the file
    df = pd.read_excel(filepath, usecols='D,F,J:J')

    # only keep rows with Duration != 0
    df = df[df.Duration != 0]

    # convert epochs from milisecs to secs
    df['Real First Packet'] = df['Real First Packet'] / 1000

    # only keep rows in between Monday Feb 4, 8 am and Friday Feb 15, 5 pm
    df = df[(df['Real First Packet'] > Mon4feb8am) & (df['Real First Packet'] < Fri15feb5pm)]

    # create new column 'doctets/Duration'
    df['doctets/Duration'] = (df.doctets / df.Duration) * 1000

    # drop columns doctets and Duration as they are no longer needed
    df.drop(['doctets', 'Duration'], axis=1, inplace=True)

    # path to save the processed file and change format from .xlsx to .csv
    output_path = preprocessed_filepath + filename
    output_path = output_path.replace("xlsx", "csv")

    df.to_csv(output_path, index=False)
