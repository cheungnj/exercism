def is_armstrong(number):
    num_string = str(number)

    value = 0
    length = len(num_string)
    for c in num_string:
        digit = int(c)
        value += digit**length
        if value > number:
            return False

    return value == number
