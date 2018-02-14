squares = {}
sums = {}


def get_square(n):
    if n in squares:
        return squares[n]

    squares[n] = n * n
    return squares[n]


def square_of_sum(count):
    if count in sums:
        return sums[count]

    total = 0
    for i in xrange(count):
        total += i + 1

    sums[count] = total * total
    return sums[count]


def sum_of_squares(count):
    total = 0
    for i in xrange(count):
        total += get_square(i + 1)

    return total


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
