def nucleotide_count():
    f = input('what is the name of your input file? ')
    with open(f) as dna:
        for line in dna:
            a_count = line.count('A')
            t_count = line.count('T')
            c_count = line.count('C')
            g_count = line.count('G')
        print(f'{a_count} {c_count} {g_count} {t_count}')


nucleotide_count()
