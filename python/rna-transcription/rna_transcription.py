def to_rna(dna_strand):
    nucleotide_map = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }
    rna_strand = ''
    for nucleotide in dna_strand:
        if nucleotide not in nucleotide_map:
            raise ValueError('{} is not a valid DNA nucleotide')

        rna_strand = rna_strand + nucleotide_map[nucleotide]

    return rna_strand
