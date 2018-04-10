from tree import Person


def text_reader(filename):
    with open(filename, 'r') as txtfile:
        # read and sort lines numerically by generation number
        lines = sorted(txtfile.readlines())
        # now the root will be established
        for line in lines:  # for loop to iterate through each line
            text = line.split(",")  # split each line
            if int(line[0]) == 0:
                p = Person(text[1].strip(), text[2].strip(), text[4].strip())  # this is to skip the first line since it has been used
                continue
            if len(line) == 0:  # break out if the line is empty (extra line is saved in text files)
                break
            if text[3] == 'M':
                p.findPerson(text[2].strip()).addChildren(text[1].strip(), text[4].strip())
            p.findPerson(text[2].strip()).addChildren(text[1].strip(), None)  # add children to the new 'root'

    return p
