from datasetImporter import create_filepath


def dna_string_import():
    dna_string_list = []
    with open(create_filepath()) as file:
        for line in file:
            clean_line = line.rstrip('\n')
            dna_string_list.append(clean_line)
        return dna_string_list

def hamm_distance(dna_string_list):
    hamm_count = 0
    for x, y in zip(dna_string_list[0], dna_string_list[1]):
        if x != y:
            hamm_count += 1
    print(hamm_count)


hamm_distance(dna_string_import())