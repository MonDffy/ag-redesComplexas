import pandas
import networkx
import matplotlib.pyplot as plt

path = r"dados\fiscalizacao_eletronica_jan2021.csv"
dataFrame = pandas.read_csv(path)
print(dataFrame.head(2))

graph = networkx.Graph()
graph.add_node(1)
graph.add_nodes_from([2, 3, 4])
graph.add_edge(1, 2)
graph.add_edges_from([(2, 3), (3, 4)])
# print(graph)
node_list = graph.nodes()
# print(node_list)

networkx.draw(graph, with_labels=True, font_weight='bold')
plt.show()  