from graphviz import Digraph


def visualizer(filename):
    familyTree = Digraph('My Family Tree', filename='visualize.gv')
    with open(filename, 'r') as txtfile:
        lines = sorted(txtfile.readlines())
        dictionary = dict()
        for line in lines:
            text = line.split(",")
            familyTree.attr('node', shape='box', color='blue')
            childname = text[1]
            parentname = text[2]
            if text[2] == "None":
                dictionary[text[1].strip()] = text[1].strip() + "\nMarried to " + text[4].strip()
                continue
            else:
                if text[3] == 'M':
                    childname += "\nMarried to " + text[4].strip()

                dictionary[text[1].strip()] = childname
                familyTree.edge(dictionary[parentname], childname)

    familyTree.render('Final_Project/visualize.gv', view=True)
