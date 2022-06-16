import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()
graph.add_node("teste")

networkx.draw(graph, with_labels=True, font_weight='bold')
plt.show()
