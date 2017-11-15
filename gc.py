from datasetImporter import create_filepath


def sequences():
    DNA_dict = {}
    DNA_string = ''
    with open(create_filepath()) as file:
        for line in file:
            if line[0] == '>' and len(DNA_string) > 0:
                DNA_dict[DNA_key] = DNA_string
                DNA_key = line[1:].rstrip('\n')
                DNA_string = ''
                if DNA_key not in DNA_dict:
                    DNA_dict[DNA_key] = None

            elif line[0] != '>':
                DNA_string += line.rstrip('\n')

            else:
                DNA_dict[line[1:].rstrip('\n')] = None
                DNA_key = line[1:].rstrip('\n')

        if DNA_dict[DNA_key] == None:
            DNA_dict[DNA_key] = DNA_string
        return DNA_dict


def max_gc_percent(DNA_dict):
    max_percent = 0
    max_percent_key = ''
    gc_percent = 0

    for k,v in DNA_dict.items():
        strip_AT = v.translate({ord(c): None for c in'AT'}) #Create a translation table - ord returns the unicode number for c
        gc_percent = float((len(strip_AT) / len(v)) * 100)

        if gc_percent > max_percent:
            max_percent = gc_percent
            max_percent_key = k

    print(max_percent_key + '\n' + str(max_percent))


max_gc_percent(sequences())











