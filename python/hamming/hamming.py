def distance(strand_a, strand_b):
    length = len(strand_a)
    if length != len(strand_b):
        raise ValueError('Strands much be of equal length')

    hamming_distance = 0
    for i in range(length):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1

    return hamming_distance
