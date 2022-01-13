from tabulate import tabulate
import pandas as pd

"""
This class is created to filter all the data from a given dataset in cvs format and print the data on the console with
the help of the single method in the class
"""


class Filter:

    """
    the method iterates through the data of a cvs file which is formatted by a DictReader and adds all the values into
    an Array called 'data', then it prints the data formatted on the console.

    Requires:   cvs files have to be formatted with DictReader
                the values in the cvs file have to be separated by a semicolon

    Ensures:    After execution of the method the console will show all data of the cvs file in a formatted way
                all the data will be saved in an array called 'data' as Strings
    """
    # TODO: new Commentation, printing all columns inline
    def print_full(dataset):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print(dataset)