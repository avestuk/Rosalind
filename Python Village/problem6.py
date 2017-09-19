import create_filepath from datasetImporter

def word_counter():
    with open(create_filepath()) as file:
        counter = {}
        for line in file:
            for word in line.split(' '):
                if word not in counter:
                    counter[word] = 1
                else:
                    counter[word] += 1
            for k,v in counter.items():
                print(k,v)


#word_counter()

print(sys.path)