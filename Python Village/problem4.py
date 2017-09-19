def sum_odds(int_tuple):
    a,b = int_tuple
    count = 0
    for x in range(a, b + 1):   # Loop through numbers from a -> b
        if x % 2 == 1:          # Determine whether the number is odd
            count += x          # if the number is odd then add it to the count
    return count


def test_sum():
    assert sum_odds((1, 10)) == 25
    #assert sum_odds((100, 200)) == 7500


input_tuple = 4550,8556
#input_tuple = 100,200

print(sum_odds(input_tuple))


