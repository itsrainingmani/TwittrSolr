with open('newGerman.txt', 'r') as istr:
    with open('new_german_output.txt', 'w') as ostr:
        for i, line in enumerate(istr):
            line = line.rstrip('\n') + ','
            ostr.write(line + '\n')
