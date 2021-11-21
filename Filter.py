from tabulate import tabulate


class Filter:

    """
    the method iterates through the data of a cvs file which is formatted by a DictReader and adds all the values into
    an Array called 'data', then it prints the data formatted on the console.

    Requires:   cvs files have to be formatted with DictReader
                the values in the cvs file have to be separated by a semicolon

    Ensures:    After execution of the method the console will show all data of the cvs file in a formatted way
                all the data will be saved in an array called 'data' as Strings
    """

    def filterCvs(self, fileReader):
        data = []

        for item in fileReader:
            data.append(item)

        print(tabulate(data))