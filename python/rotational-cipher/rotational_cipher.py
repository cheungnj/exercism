import string


lower_start = ord('a') - 1
lower_end = ord('z')
upper_start = ord('A') - 1
upper_end = ord('Z')


def rotate(text, key):
    key = key % 26
    if key == 0:
        return text

    encoded = ''
    for char in text:
        if char not in string.ascii_letters:
            encoded += char
            continue

        value = ord(char)
        value += key
        lower_bound = lower_start if char in string.ascii_lowercase else upper_start
        upper_bound = lower_end if char in string.ascii_lowercase else upper_end
        if value > upper_bound:
            value -= upper_bound
            value += lower_bound

        encoded += chr(value)

    return encoded
