from DataFrame import dfAcidentes, dfFiscalizacao
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

nodes = []
edge1 = []
edge2 = []
var = 0

while (var < dfAcidentes['nome_logradouro'].size):
    if (dfAcidentes['nome_logradouro'].iloc[var] in nodes):
        var += 1
        continue
    if (
        dfAcidentes['nome_logradouro'].str.replace("  ", "").iloc[var] not in nodes
    ):
        nodes.append(
            dfAcidentes['nome_logradouro'].str.replace("  ", "").iloc[var]
        )
    var += 1

graph.add_nodes_from(nodes)

var = 0
aux = ""

while (var < len(nodes)):
    aux = nodes[var]
    aux = aux.replace(" ", "")
    for i in range(dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size -1):
        if (
            dfFiscalizacao[
                'DESC_LOC_CONTROLADOR_TRANSITO'
            ].str.upper().str.replace(" ", "").str.contains(aux).iloc[i] and
            nodes[var] not in edge1
        ):
        
            edge1.append(
                nodes[var]
            )
    for i in range(dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size):
        if (
            dfFiscalizacao[
                'DESC_LOC_CONTROLADOR_TRANSITO'
            ].str.upper().str.replace(" ", "").str.contains(nodes[var]).iloc[i] and
            nodes[var] not in edge2 and
            nodes[var] not in edge1[var]
        ):
            edge2.append(
                nodes[var]
            )
    var += 1


for u,v, in zip(edge1, edge2):
    graph.add_edge(u, v)

print (edge1)
print ()
print (edge2)

networkx.drs
