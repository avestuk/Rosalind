from datasetImporter import create_filepath


def substring_position():
    args = []
    with open(create_filepath()) as file:
        for line in file:
            args.append(line)
    s = args[0].strip('\n')
    t = args[1].strip('\n')
    index = 0
    substring_pos_list = []
    while True:
        if s.find(t,index) >= 0:
            substring_pos_list.append((s.find(t, index)) + 1) # need to add 1 to this. It's base 1 not 0
            index = s.find(t,index) + 1
        else:
            print(*substring_pos_list)
            break



substring_position()


