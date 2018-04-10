from graphviz import Digraph
from txt_reader import text_reader
import argparse


parser = argparse.ArgumentParser(
    description='grabbing elements from the tree or visualizing it',
    formatter_class=argparse.RawTextHelpFormatter,
    )

parser.add_argument("--visualize",
    help="Will display the tree",
    dest='vis')

parser.add_argument("--get",
    help="Will get a desired component from a desired person",
    choices=['siblings', 'parents', 'spouse', 'children'],
    default='parents',
    dest='get')

t = text_reader('family_tree.txt')
args = parser.parse_args()

if args.vis is not None:
    familyTree = Digraph('My Family Tree', filename='txt_reader.gv')
    familyTree.render('Final_Project/txt_reader.gv', view=True)

if args.get == "parents":
    ans = input("Whose Parents would you like to find? ")
    if t.findPerson(ans) is None:
        print("That person isn't in the tree, sorry.")
    elif t.getParents(ans) is None:
        print("This person's Parents are not in the tree.")
    else:
        print("The parents of ", ans, "are ")
        print(*t.getParents(ans))

if args.get == "siblings":
    ans = input("Whose siblings would you like to find? ")
    if t.findPerson(ans) is None:
        print("That person isn't in the tree, sorry.")
    elif len(t.getSiblings(ans)) == 0:
        print("This person is an only child")
    else:
        print(ans, "has ", len(t.getSiblings(ans)), " sibling(s): ")
        print(*t.getSiblings(ans))

if args.get == "spouse":
    ans = input("Whose spouse would you like to find? ")
    if t.findPerson(ans) is None:
        print("That person isn't in the tree, sorry.")
    elif t.getSpouse(ans) is None:
        print("This person is not married.")
    else:
        print(ans, " is married to ", t.getSpouse(ans))

if args.get == "children":
    ans = input("Whose children would you like to find? ")
    if t.findPerson(ans) is None:
        print("That person isn't in the tree, sorry.")
    elif len(t.findPerson(ans).children) == 0:
        print("This person has no kids.")
    else:
        print(ans, " has", len(t.findPerson(ans).children, "kid(s): "))
        print(*t.findPerson.getAllChildren(ans))
