from datasetImporter import create_filepath



def rna_codons():
    rna_codon = {}
    with open(create_filepath()) as file:
        for line in file:
            rna_codon[line.split()[0]] = line.split()[1]
        return rna_codon


def rna_string():
    with open(create_filepath()) as file:
        for line in file:
            return line.rstrip('\n')


def rna_codon_mapping():
    protein_string = ''
    rna_codon_map = rna_codons()
    RNA_string = rna_string()
    i = 0
    while i < len(RNA_string):
        if RNA_string[i:i + 3] in rna_codon_map.keys():
            if rna_codon_map[RNA_string[i:i + 3]] == 'Stop':
                break
            slice = RNA_string[i:i + 3]
            protein_string += rna_codon_map[RNA_string[i:i + 3]]
            i += 3
    print(protein_string)


rna_codon_mapping()
