def is_pangram(sentence):
    if len(sentence) < 26:
        return False

    # or use set(list(string.ascii_lowercase))
    alphabet = set([
        'a', 'b', 'c', 'd', 'e', 'f',
        'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's',
        't', 'u', 'v', 'w', 'x', 'y', 'z'
    ])

    s = sentence.lower()
    for c in s:
        try:
            alphabet.remove(c)
        except KeyError:
            pass

    return len(alphabet) == 0
