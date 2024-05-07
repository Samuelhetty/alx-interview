#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    operations = 0
    clipboard = 0
    curr_length = 1
    # print('H', end='')
    while curr_length < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = curr_length
            curr_length += clipboard
            operations += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - curr_length > 0 and (n - curr_length) % curr_length == 0:
            # copy all and paste
            clipboard = curr_length
            curr_length += clipboard
            operations += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif clipboard > 0:
            # paste
            curr_length += clipboard
            operations += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return operations
