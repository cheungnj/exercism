def is_isogram(string):
    chars = set()
    for c in string:
        c = c.lower()
        if c in (' ', '-'):
            continue
        if c in chars:
            return False
        chars.add(c)
    return True
