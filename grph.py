from datasetImporter import create_filepath


def make_dict():
    dna_dict = {}
    dna_string = ''
    with open(create_filepath()) as file:
        for line in file:
            if line[0] == '>' and len(dna_string) > 0:
                dna_dict[DNA_key] = dna_string
                DNA_key = line[1:].rstrip('\n')
                dna_string = ''
                if DNA_key not in dna_dict:
                    dna_dict[DNA_key] = None

            elif line[0] != '>':
                dna_string += line.rstrip('\n')

            else:
                dna_dict[line[1:].rstrip('\n')] = None
                DNA_key = line[1:].rstrip('\n')

        if dna_dict[DNA_key] == None:
            dna_dict[DNA_key] = dna_string
        return dna_dict

def grph(dna_dict):             # Need a function that'll compare the last 3 characters of one key to the first 3 of the other keys.
    for v in dna_dict.values():
        if v[len(v)-3:] in dna_dict.values()[:4]:
            break

grph(make_dict())


