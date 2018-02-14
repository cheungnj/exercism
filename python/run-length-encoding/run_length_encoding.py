from string import digits


def decode(string):
    decoded = ''
    digit_str = ''
    for char in string:
        if char in digits:
            digit_str += char
            continue
        s = char
        if digit_str:
            s = int(digit_str) * s
        decoded += s
        digit_str = ''

    return decoded


def encode(string):
    encoded = ''
    prev = ''
    count = 1
    for char in string:
        if not prev:
            prev = char
            continue
        if char == prev:
            count += 1
            continue
        if count > 1:
            encoded += str(count)
        encoded += prev
        prev = char
        count = 1
    if count > 1:
        encoded += str(count)
    encoded += prev

    return encoded
