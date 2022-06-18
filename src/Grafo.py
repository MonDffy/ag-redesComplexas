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

while (var < dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size):
    for i in range(edge1.size -1):
        if (
            dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper().str.replace("  ", "").str.contains(edge1[i].str.upper().str.replace("  ", "")).iloc[var]
        ): 
            for j in range(nodes.size - 1):
                if (
                    dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper().str.replace("  ", "").str.contains(nodes[j].str.upper().str.replace("  ", "")).iloc[var]
                ):
                    edge2.append(nodes[j])
    var += 1
print (edge2)

# for i in range(edge1.size - 1):
#     for j in range(nodes.size - 1):
#         if (
#             nodes[i].str.upper.str.replace("  ", "") in dfAcidentes['nome_logradouro'].str.upper.str.replace("  ", "").iloc[j]
#         ):
#             edge2[i] = nodes[i]
#             continue
# print (edge2)

# while (var < dfAcidentes['nome_logradouro'].size):
#     if (dfAcidentes['nome_logradouro'].iloc[var] in nodes):
#         var += 1
#         continue
#     if (
#         dfAcidentes['nome_logradouro'].str.replace("  ", "").iloc[var] not in nodes
#     ):
#         nodes.append(
#             dfAcidentes['nome_logradouro'].str.replace("  ", "").iloc[var]
#         )
#     var += 1

# while (var < len(nodes)):
#     aux = nodes[var]
#     aux = aux.replace(" ", "")
#     for i in range(dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size - 1):
#         if (
#             dfFiscalizacao[
#                 'DESC_LOC_CONTROLADOR_TRANSITO'
#             ].str.upper().str.replace(" ", "").str.contains(aux).iloc[i] and
#             nodes[var] not in edge1
#         ):
#             edge1.append(
#                 nodes[var]
#             )
#     var += 1

# var = 0

# while (var < len(nodes)):
#     aux1 = nodes[var]
#     aux1 = aux.replace(" ", "")
#     for i in range(dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size - 1):
#         for j in range(len(edge1) - 1):
#             aux2 = edge1[j]
#             aux2 = aux2.replace(" ", "")
#             if (
#                 aux1 != aux2 and
#                 aux1 not in edge2 and
#                 dfFiscalizacao[
#                     'DESC_LOC_CONTROLADOR_TRANSITO'
#                 ].str.upper().str.replace(" ", "").str.contains(aux1).iloc[i] and
#                 dfFiscalizacao[
#                     'DESC_LOC_CONTROLADOR_TRANSITO'
#                 ].str.upper().str.replace(" ", "").str.contains(aux2).iloc[i]
#             ):
#                 edge2.append(
#                     nodes[var]
#                 )
#     var += 1

# for u, v, in zip(edge1, edge2):
#     graph.add_edge(u, v)

# print(edge1)
# print()
# print(edge2)

# networkx.draw(graph, with_labels=True, font_weight='bold')
# plt.show()
