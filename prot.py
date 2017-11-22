from datasetImporter import create_filepath


def rna_codons():
    rna_codon = {}
    with open(create_filepath()) as file:
        for line in file:
            rna_codon[line.split()[0]] = line.split()[1]  # set
        return rna_codon


def rna_string():
    with open(create_filepath()) as file:
        for line in file:
            return line.rstrip('\n')


def rna_codon_mapping():
    protein_string = ''
    rna_codon_map = rna_codons()
    for x in rna_string()[::3]:
        protein_string += rna_codon_map[x]
    return protein_string

