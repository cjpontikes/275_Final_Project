from graphviz import Digraph


def visualizer(filename):
    familyTree = Digraph('My Family Tree', filename='visualize.gv')
    with open(filename, 'r') as txtfile:
        lines = sorted(txtfile.readlines())
        # print(lines)
        for line in lines:
            text = line.split(",")
            familyTree.attr('node', shape='box', color='blue')
            if text[2] == "None":
                familyTree.node(text[1].strip())
                continue
            if text[3] == 'M':
                familyTree.node(text[1].strip(), xlabel="Married To " + text[4])
            familyTree.node(text[1].strip(), text[1].strip())
            if text[2] is not None:
                # print("make connection")
                familyTree.edge(text[2], text[1])

    familyTree.render('Final_Project/visualize.gv', view=True)
