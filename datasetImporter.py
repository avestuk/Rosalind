import os, itertools


def create_filepath():
    filename = input('What is your input file called? ')
    script_dir = os.path.dirname(__file__)
    file_dir = '/Datasets/'
    filepath = file_dir + filename
    absolute_filepath = script_dir + filepath
    return absolute_filepath


def import_two_integers():
    with open(create_filepath()) as file:
        for line in file:
            a_delimiter = line.find(' ')
            a = int(line[:a_delimiter])
            b = int(
                ''.join(itertools.takewhile(str.isdigit, line[a_delimiter + 1:])))  # Take characters from the string
            # while they are digits
            return a, b
