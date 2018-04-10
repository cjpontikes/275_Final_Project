from competitor import Competitor
from graphviz import Digraph

bracket = Digraph("Tournament Bracket", filename='tournament_bracket.gv')

bracket.node('A', 'Mario')
bracket.node('B', 'Luigi')
bracket.node('C', 'Wario')
bracket.node('D', 'Waluigi')
bracket.node('E', 'Mario')
bracket.node('F', 'Waluigi')
bracket.edge('A', 'C', constraint='false')
bracket.edge('B', 'D', constraint='false')
bracket.edge('E', 'A')
bracket.edge('E', 'B')
bracket.edge('F', 'C')
bracket.edge('F', 'D')
bracket.edge('E', 'F')

print("hello???")
print(bracket.source)
bracket.render('Final_Project/tournament_bracket.gv', view=True)
