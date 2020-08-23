import pandas as pd
from os import listdir

Mon4feb8am = 1359982800  # Timestamp on Monday Feb 4 8:00:00 am Local Time zone
Mon11feb8am = 1360587600  # Timestamp on Monday Feb 11 8:00:00 am Local Time zone
# Fri15feb5pm = 1360965600  # Timestamp on Friday Feb 15 5:00:00 pm Local Time zone

preprocessed_filepath = '../preprocessed_files/'
wind10sec_path = '../processed_files/10sec_file/'
wind227sec_path = '../processed_files/227sec_file/'
wind300sec_path = '../processed_files/300sec_file/'


# daily number of windows from 8:00:00 am to 5:00:00 pm ( 9 hours = 32400 secs) = int(32400 / window size)


# This function calculates a list containing windows, then calls the function window_value_calculator()
# for each file which returns two lists containing doctets/duration and and week for corresponding window
# for each window size (winsize) and saves that into new data file in the folder for that respective window size.
def window_generator(winsize):
    daily_windows = int(32400 / winsize)  # Windows per day
    day = 0
    wind_series = []
    week = []
    # Calculate the Windows and Week data
    while day < 10:
        # Day is in first week (first 5 days Mon to Fri)
        if day < 5:
            morning8am = Mon4feb8am + day * 86400  # a day has 86400 seconds, and starting from Mon 4 Feb
            for w in range(daily_windows):
                # create an epoch for beginning of every window
                epoch = morning8am + w * winsize
                wind_series.append(epoch)
                week.append('Week1')
        # for next week
        else:
            morning8am = Mon11feb8am + (day - 5) * 86400
            for w in range(daily_windows):
                epoch = morning8am + w * winsize
                wind_series.append(epoch)
                week.append('Week2')
        day += 1

    num = 0
    df = pd.DataFrame({'window_start': wind_series, 'week': week})
    file_list = [f for f in listdir(preprocessed_filepath) if not (f.startswith('.') or f.startswith('~'))]

    for file in file_list:

        num += 1

        # Call window_value_calculator for every file
        docperdur = window_value_calculator(file, winsize, wind_series)

        print(winsize, "Sec  File", num, " Processed")
        newcolname = file.strip('.csv')

        # add new column to the dataframe containing doctets per duration for the current file
        df[newcolname] = docperdur

    new_path = None
    if winsize == 10:
        new_path = wind10sec_path + 'all_user_10sec.csv'
    elif winsize == 227:
        new_path = wind227sec_path + 'all_user_227sec.csv'
    elif winsize == 300:
        new_path = wind300sec_path + 'all_user_300sec.csv'

    df.to_csv(new_path, index=False)


# This Function calculates the value of doctets/duration for a window and returns a list
def window_value_calculator(filename, winsize, wind_series):

    filepath = preprocessed_filepath + filename
    df = pd.read_csv(filepath)

    # get the [Real First Packet] column in a list, convert to int (drop decimals) and sort it
    first_pkt_list = df['Real First Packet'].tolist()
    first_pkt_list = list(map(int, first_pkt_list))
    first_pkt_list.sort()

    # get the [doctets/Duration] column in a list
    orgdocdur = df['doctets/Duration'].tolist()

    docperdur = []  # To store Doctets/Duration for a window
    rowindex = 0    # index to use on first pkt list

    # record data corresponding to every window
    for i in range(len(wind_series)):


        while rowindex < len(first_pkt_list):

            # to check if the first pkt list element is behind the time window
            if first_pkt_list[rowindex] < wind_series[i]:

                # Move on to the next first pkt
                rowindex += 1

            else:
                break

        total = 0
        count = 0
        while rowindex < len(first_pkt_list):

            # if elements fall in the window
            if wind_series[i] <= first_pkt_list[rowindex] < wind_series[i] + winsize:
                # Add docts/dur for that row
                total += orgdocdur[rowindex]
                # increase the count of elements found
                count += 1
                # move on to the next first pkt
                rowindex += 1

            else:
                # Break the loop and go back to the upper loop to move to next window
                break

        if count > 0:              # If first pkt elements found in the window
            total = total / count  # Averaging docts per duration for that window

        else:
            total = 0.001

        docperdur.append(total)

    return docperdur
