import pytest


def splicer(a, b, c, d, string):
    a_b = string[a:b + 1]
    c_d = string[c:d + 1]
    return a_b + ' ' + c_d


def test_output():
    assert splicer(22, 27, 97, 102,
                   'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.') == 'Humpty Dumpty'


print(splicer(84, 89, 119, 125,
              '7WlLzctSRhdDMw7QFah3hQxzDox3vuWa29bMzczap9h2d6ybbbR6bTnuzP5Pk9pnvDsCj1M7XcJlV7xGnv4rAythyaXUDabM7EQgP1MixpQZdHhifM7fOy8pulchraRelF8dY0YxOU7897xfWHr3vGKb7kxSmr43BotdzUsQNT.'))
