import pandas
from DataFrame import dfAcidentes, dfFiscalizacao
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

nodes = []
nodesColors = [(0.93,0,0.07), #Cor de cada um dos vértices em RGB decimal, indo de 0-1
               (0.78,0,0.22),
               (0.84,0,0.26),
               (0.49,0,0.51),
               (0.77,0,0.23),
               (0.76,0,0.24),
               (0.91,0,0.1),
               (0.94,0,0.06),
               (0.81,0,0.19),
               (0.95,0,0.05),
               (0.64,0,0.36),
               (0.81,0,0.19),
               (0.75,0,0.25),
               (0.75,0,0.25),
               (0.86,0,14)]
aux= []
filter = [               'AFONSO PENA                                       ' , #Filtro para pegar somente as ruas que tem dados nas duas tabelas
                         'SANTA CATARINA                                    ' ,
                         'AMAZONAS                                          ' ,
                         'CURITIBA                                          ' ,
                         'DO CONTORNO                                       ' ,
                         'DOS ANDRADAS                                      ' ,
                         'SAO PAULO                                         ' ,
                         'ALVARES CABRAL                                    ' ,
                         'DA BAHIA                                          ' ,
                         'CARANDAI                                          ' ,
                         'ESPIRITO SANTO                                    ' , 
                         'DOS GUAICURUS                                     ' ,
                         'AUGUSTO DE LIMA                                   ' ,
                         'MATO GROSSO                                       ' ,
                         'BIAS FORTES                                       ']

edgeSaoPaulo = [('SAO PAULO                                         ','DO CONTORNO                                       '),
                ('SAO PAULO                                         ','ALVARES CABRAL                                    '),
                ('SAO PAULO                                         ','BIAS FORTES                                       '),
                ('SAO PAULO                                         ','AUGUSTO DE LIMA                                   '),
                ('SAO PAULO                                         ','AMAZONAS                                          '),
                ('SAO PAULO                                         ','AFONSO PENA                                       '),
                ('SAO PAULO                                         ','DOS CAETES                                        '),
                ('SAO PAULO                                         ','SANTOS DUMONT                                     '),
                ('SAO PAULO                                         ','DOS GUAICURUS                                     ')]
                

edgeSantaCatarina = [('SANTA CATARINA                                    ','DO CONTORNO                                       '),
                     ('SANTA CATARINA                                    ','ALVARES CABRAL                                    '),
                     ('SANTA CATARINA                                    ','BIAS FORTES                                       '),
                     ('SANTA CATARINA                                    ','AUGUSTO DE LIMA                                   '),
                     ('SANTA CATARINA                                    ','AMAZONAS                                          ')
]
edgeAlveresCabral = [('ALVARES CABRAL                                    ','DO CONTORNO                                       '),
                     ('ALVARES CABRAL                                    ','DA BAHIA                                          '),
                     ('ALVARES CABRAL                                    ','AUGUSTO DE LIMA                                   '),
                     ('ALVARES CABRAL                                    ','AFONSO PENA                                       '),
                     ('ALVARES CABRAL                                    ','ESPIRITO SANTO                                    '),
                     ('ALVARES CABRAL                                    ','CURITIBA                                          ')]

edgeAmazonas = [('AMAZONAS                                          ','DO CONTORNO                                       '),
                ('AMAZONAS                                          ','MATO GROSSO                                       '),
                ('AMAZONAS                                          ','CURITIBA                                          '),
                ('AMAZONAS                                          ','AFONSO PENA                                       '),
                ('AMAZONAS                                          ','ESPIRITO SANTO                                    ')]

edgeAndradas = [('DOS ANDRADAS                                      ','DO CONTORNO                                       ')]

edgeAfPena = [( 'AFONSO PENA                                       ','CURITIBA                                          '),
               ('AFONSO PENA                                       ','DO CONTORNO                                       '),
               ('AFONSO PENA                                       ','DA BAHIA                                          '),
               ('AFONSO PENA                                       ','ESPIRITO SANTO                                    '),
               ('AFONSO PENA                                       ','CARANDAI                                          ')]

edgeGuaicurus = [('DOS GUAICURUS                                     ','CURITIBA                                          '),
                 ('DOS GUAICURUS                                     ','DA BAHIA                                          ')]

edgeEspiritoSanto = [('ESPIRITO SANTO                                    ','DO CONTORNO                                       '),
                     ('ESPIRITO SANTO                                    ','BIAS FORTES                                       '),
                     ('ESPIRITO SANTO                                    ','AUGUSTO DE LIMA                                   ')]


edgeAugustoLima = [('AUGUSTO DE LIMA                                   ','DO CONTORNO                                       '),
                   ('AUGUSTO DE LIMA                                   ','MATO GROSSO                                       '),
                   ('AUGUSTO DE LIMA                                   ','CURITIBA                                          '),
                   ('AUGUSTO DE LIMA                                   ','DA BAHIA                                          ')]

edgeCuritiba = [('CURITIBA                                          ','DO CONTORNO                                       '),
                ('CURITIBA                                          ','BIAS FORTES                                       ')]

edgeContorno = [('DO CONTORNO                                       ','BIAS FORTES                                       '),
                ('DO CONTORNO                                       ','CARANDAI                                          ')]

edgeMGrosso = [('MATO GROSSO                                       ','BIAS FORTES                                       ')]

edgeBiasFortes = [('BIAS FORTES                                       ','DA BAHIA                                          ')]


aux = dfAcidentes['nome_logradouro'].drop_duplicates('first')
for i in range (aux.size -1):
    if(aux.iloc[i] in filter):
        nodes.append(aux.iloc[i])
    
    
graph.add_nodes_from(nodes)
graph.add_edges_from(edgeSantaCatarina)
graph.add_edges_from(edgeSaoPaulo)
graph.add_edges_from(edgeAlveresCabral)
graph.add_edges_from(edgeAmazonas)
graph.add_edges_from(edgeAndradas)
graph.add_edges_from(edgeAfPena)
graph.add_edges_from(edgeEspiritoSanto)
graph.add_edges_from(edgeAugustoLima)
graph.add_edges_from(edgeCuritiba)
graph.add_edges_from(edgeContorno)
graph.add_edges_from(edgeMGrosso)
graph.add_edges_from(edgeBiasFortes)
graph.add_edges_from(edgeGuaicurus)          

networkx.draw(graph , with_labels=True, font_weight='normal')
plt.show()
