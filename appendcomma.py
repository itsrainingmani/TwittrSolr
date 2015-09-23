with open('russian.txt', 'r') as istr:
    with open('russian_output.txt', 'w') as ostr:
        for i, line in enumerate(istr):
            line = line.rstrip('\n') + ','
            ostr.write(line + '\n')
