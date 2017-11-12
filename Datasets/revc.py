def reverse_strand(dna):
    return dna[::-1]


def strand_complement(dna):
    complement = ''
    dna_complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in dna:
        complement += dna_complement[base]
    return complement


print(strand_complement(reverse_strand('AAAACCCGGT')))
