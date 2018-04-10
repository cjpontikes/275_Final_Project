from tree import Person
from graphviz import Digraph


familyTree = Digraph('My Family Tree', filename='txt_reader.gv')


def text_reader(filename):
    with open(filename, 'r') as txtfile:
        # read and sort lines numerically by generation number
        lines = sorted(txtfile.readlines())
        # now the root will be established
        for line in lines:  # for loop to iterate through each line
            text = line.split(",")  # split each line
            familyTree.attr('node', shape='box', color='blue')
            if int(line[0]) == 0:
                p = Person(text[1].strip(), text[2].strip(), text[4].strip())  # this is to skip the first line since it has been used
                familyTree.node(text[1].strip())
                continue
            if len(line) == 0:  # break out if the line is empty (extra line is saved in text files)
                break
            if text[3] == 'M':
                p.findPerson(text[2].strip()).addChildren(text[1].strip(), text[4].strip())
                familyTree.node(text[1].strip(), xlabel="Married To " + text[4])
            p.findPerson(text[2].strip()).addChildren(text[1].strip(), None)  # add children to the new 'root'
            familyTree.node(text[1].strip(), text[1].strip())
            if text[2] is not None:
                # print("make connection")
                familyTree.edge(text[2], text[1])
    return p
