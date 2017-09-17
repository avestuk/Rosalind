import os
import itertools


script_dir = os.path.dirname(__file__)
file_dir = '/Datasets/'
filename = 'rosalind_ini2.txt'
filepath = file_dir + filename
absolute_filepath = script_dir + filepath


def hypotenuse_square(a, b):
    return ((a ** 2) + (b ** 2))


with open(absolute_filepath) as file:
    for line in file:
        a_delimiter = line.find(' ')
        a = int(line[:a_delimiter])
        b = int(''.join(itertools.takewhile(str.isdigit, line[a_delimiter+1:]))) # Take characters from the string
                                                                                 # while they are digits
        print(hypotenuse_square(a,b))


def test_hypotenuse_square():
    assert hypotenuse_square(3, 4) == 25