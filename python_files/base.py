from os import listdir
from preprocessor import preprocess
from window_calc import window_generator
from calculations import perform_calc

original_filepath = '../original_files'
preprocessed_filepath = '../preprocessed_files'
windowsizes = [10, 227, 300]


def main():

    choice = input("Do you want to clean the original the files first ? (Y/N) \n")
    if choice == 'y' or choice == 'Y':
        i = 0

        # To get the list of files avoiding the hidden files that may start with '.' or '~'
        original_filelist = [f for f in listdir(original_filepath) if not (f.startswith('.') or f.startswith('~'))]

        for filename in original_filelist:
            i += 1
            print(filename)
            preprocess(filename)
            print(i, "file cleaning done")

    choice = input("Do you want to process the cleaned files ? (Y/N) \n")

    if choice == 'y' or choice == 'Y':

        for size in windowsizes:
            window_generator(size)

    perform_calc()

# ================ call main function ======================

main()

