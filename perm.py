# Need to figure out how many positive integers you have. Can simply count down to 0
# Could use this to also figure out how many place holders the list needs
# Begin creating lists by checking if an integer has already been in a position. I think that each int can be in a position n - 1 times
# Create a cache to check against then check each position
# itertools.product would probably make thi sall very easy!
from itertools import permutations
from datasetImporter import create_filepath


def perm():
    with open(create_filepath()) as file:
        for x in file:
            n = int(x)
            print(len(list(permutations(range(1, n+1)))))
            for i in permutations(range(1, n+1)):
                print(*i)


perm()
