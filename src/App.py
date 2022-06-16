import pandas
import networkx
import matplotlib.pyplot as plt

# path = r"dados\fiscalizacao_eletronica_jan2021.csv"
# dataFrame = pandas.read_csv(path)
# # print(dataFrame)

graph = networkx.Graph()
graph.add_node(1)
graph.add_nodes_from([
    (2, {"color": "red"}),
    (3, {"color": "green"})
])  
graph.add_edge(1, 2)
# graph.add_edges_from([(2, 3), (3, 4)])
# print(graph)
node_list = graph.nodes()
# print(node_list)

graph[1]

networkx.draw(graph, with_labels=True, font_weight='bold')
plt.show()
