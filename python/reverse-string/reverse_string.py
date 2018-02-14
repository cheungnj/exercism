def reverse(input=''):
    if not input:
        return ''

    length = len(input)
    s = ''
    for i in xrange(length - 1, -1, -1):
        s = s + input[i]
    return s
