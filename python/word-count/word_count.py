def word_count(phrase):
    phrase = phrase.lower().replace('\t', ' ').replace('\n', ' ').replace(',', ' ').replace('_', ' ')
    words = [s.strip() for s in phrase.split()]
    word_map = {}
    blacklist = ('.', '!', '&', '@', '$', '%', '^', '&', ':')
    for word in words:
        current_word = word
        for char in blacklist:
            current_word = current_word.replace(char, '')
        if current_word.count("'") == 2:
            current_word = current_word.replace("'", '')
        if current_word:
            count = word_map.get(current_word, 0) + 1
            word_map[current_word] = count
    return word_map
