from graphviz import Digraph
import pydotplus
from IPython.display import Image


dot = Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('C', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AC'])
dot.edge('B', 'L', constraint='false')
dot.render('round-table2.dot', view=True)