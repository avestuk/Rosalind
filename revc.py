from datasetImporter import create_filepath


def reverse_strand():  # reverse the input DNA string
    with open(create_filepath()) as file:
        for line in file:
            line = line.rstrip()  # remove trailing characters
            return line[::-1]


def strand_complement(dna):  # create the compliment strand
    complement = ''
    dna_complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in dna:
        complement += dna_complement[base]
    return complement


def reverse_complement():
    print(strand_complement(reverse_strand()))

reverse_complement()
