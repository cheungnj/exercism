def verify(isbn):
    if not isbn:
        return False

    isbn = isbn.replace('-', '')
    length = len(isbn)
    if length != 10:
        return False

    # check for bad check digit
    check_digit = 10
    try:
        check_digit = int(isbn[-1])
    except ValueError:
        if isbn[-1] != 'X':
            return False

    isbn_sum = 0
    multiplier = 10
    for c in isbn[:length - 1]:
        if c in ('-', 'X'):
            continue
        try:
            digit = int(c)
        except ValueError:
            if c not in ('-', 'X'):
                return False
            continue
        isbn_sum += digit * multiplier
        multiplier -= 1

    isbn_sum = (11 - (isbn_sum % 11)) % 11
    return isbn_sum == check_digit
