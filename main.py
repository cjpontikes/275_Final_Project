from txt_reader import text_reader
from visualize import visualizer
import argparse


parser = argparse.ArgumentParser(
    description='grabbing elements from the tree or visualizing it',
    formatter_class=argparse.RawTextHelpFormatter,
    )

parser.add_argument("--vis",
    help="Will display the tree",
    dest='vis')

parser.add_argument("--get",
    help="Will get a desired component from a desired person",
    choices=['siblings', 'parents', 'spouse', 'children', 'cousins'],
    dest='get')

t = text_reader('family_tree.txt')
args = parser.parse_args()

if args.vis:
    visualizer('family_tree.txt')


if args.get == "parents":
    ans = input("Whose Parents would you like to find? ")
    while t.findPerson(ans) is None:
        ans = input("That person isn't in the tree, sorry. Try again: ")
    if t.getParents(ans) is None:
        print(ans, "has no parents in the tree.")
    else:
        print("The parents of ", ans, "are: ")
        print(", ".join(t.getParents(ans)))

if args.get == "siblings":
    ans = input("Whose siblings would you like to find? ")
    while t.findPerson(ans) is None:
        ans = input("That person isn't in the tree, sorry. Try agian: ")
    if t.getSiblings(ans) is None:
        print(ans,"has no siblings in the tree.")
    elif len(t.getSiblings(ans)) == 0:
        print(ans, "is an only child")
    else:
        print(ans, "has ", len(t.getSiblings(ans)), " sibling(s): ")
        print(", ".join(t.getSiblings(ans)))

if args.get == "spouse":
    ans = input("Whose spouse would you like to find? ")
    while t.findPerson(ans) is None:
        ans = input("That person isn't in the tree, sorry. Try again: ")
    if t.getSpouse(ans) is None:
        print(ans," is not married")
    else:
        print(ans, " is married to ", t.getSpouse(ans))

if args.get == "children":
    ans = input("Whose children would you like to find? ")
    while t.findPerson(ans) is None:
        ans = input("That person isn't in the tree, sorry. Try again: ")
    if len(t.findPerson(ans).children) == 0:
        print(ans, " has no kids.")
    else:
        print(ans, " has", len(t.findPerson(ans).children), "kid(s): ")
        print(", ".join(t.getAllChildren(ans)))

if args.get == 'cousins':
    ans = input("Whose cousins would you like to find? ")
    while t.findPerson(ans) is None:
        ans = input("That person isn't in the tree, sorry. Try again: ")
    if t.getFirstCousins(ans) is None:
        print(ans, "has no first cousins in the tree.")
    elif len(t.getFirstCousins(ans)) == 0:
        print(ans, "has no first cousins.")
    else:
        print(ans, " has", len(t.getFirstCousins(ans)), "first cousin(s): ")
        print(", ".join(t.getFirstCousins(ans)))
