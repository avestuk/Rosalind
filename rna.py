from datasetImporter import create_filepath


def dna_to_rna():
    rna = ''
    with open(create_filepath()) as file:
        for line in file:
            for nucleotide in line:
                if nucleotide == 'T':
                    rna += 'U'
                else:
                    rna += nucleotide
        return rna

print(dna_to_rna())
