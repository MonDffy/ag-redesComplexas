import pandas
from DataFrame import dfAcidentes, dfFiscalizacao
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

nodes = []
edge1 = []
edge2 = []
var = 0

nodes = dfAcidentes['nome_logradouro'].drop_duplicates('first')

graph.add_nodes_from(nodes)

edge1 = nodes
for i in range(edge1.size - 1):
    edge2.append("")

# while (var < dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size):
#     for i in range(edge1.size -1):
#         if (
#             dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper().str.replace("  ", "").str.contains(edge1[i].str.upper().str.replace("  ", "")).iloc[var]
#         ): 
#             for j in range(nodes.size - 1):
#                 if (
#                     dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper().str.replace("  ", "").str.contains(nodes[j].str.upper().str.replace("  ", "")).iloc[var]
#                 ):
#                     edge2.append(nodes[j])
#     var += 1
# print (edge2)

networkx.draw(graph, with_labels=True, font_weight='bold')
plt.show()
