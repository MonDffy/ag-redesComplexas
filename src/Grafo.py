from turtle import color
import pandas
from DataFrame import dfAcidentes, dfFiscalizacao
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

nodes = []
color_map = [(0.311, 0, 0.05, 1),  # Cor de cada um dos vértices em RGBA decimal, indo de 0-1
               (0.08, 0, 0.05, 1),
               (0.05, 0, 0.02, 1),
               (0.462, 0, 1, 1),
               (0.430, 0, 0.261, 1),
               (1, 0, 0.63, 1),
               (0.225, 0, 0.05, 1),
               (0.301, 0, 0.05, 1),
               (0.183, 0, 0.09, 1),
               (0.354, 0, 0.05, 1),
               (0.634, 0, 0.72, 1),
               (0.097, 0, 0.05, 1),
               (0.130, 0, 0.09, 1),
               (0.161, 0, 0.11, 1),
               (0.280, 0, 0.09, 1),
               ]
aux = []
filter = ['AFONSO PENA                                       ',  # Filtro para pegar somente as ruas que tem dados nas duas tabelas
          'SANTA CATARINA                                    ',
          'AMAZONAS                                          ',
          'CURITIBA                                          ',
          'DO CONTORNO                                       ',
          'DOS ANDRADAS                                      ',
          'SAO PAULO                                         ',
          'ALVARES CABRAL                                    ',
          'DA BAHIA                                          ',
          'CARANDAI                                          ',
          'ESPIRITO SANTO                                    ',
          'DOS GUAICURUS                                     ',
          'AUGUSTO DE LIMA                                   ',
          'MATO GROSSO                                       ',
          'BIAS FORTES                                       ']

edgeSaoPaulo = [('SAO PAULO                                         ', 'DO CONTORNO                                       '),
                ('SAO PAULO                                         ',
                 'ALVARES CABRAL                                    '),
                ('SAO PAULO                                         ',
                 'BIAS FORTES                                       '),
                ('SAO PAULO                                         ',
                 'AUGUSTO DE LIMA                                   '),
                ('SAO PAULO                                         ',
                 'AMAZONAS                                          '),
                ('SAO PAULO                                         ',
                 'AFONSO PENA                                       '),
                ('SAO PAULO                                         ', 'DOS GUAICURUS                                     ')]


edgeSantaCatarina = [('SANTA CATARINA                                    ', 'DO CONTORNO                                       '),
                     ('SANTA CATARINA                                    ',
                      'ALVARES CABRAL                                    '),
                     ('SANTA CATARINA                                    ',
                      'BIAS FORTES                                       '),
                     ('SANTA CATARINA                                    ',
                      'AUGUSTO DE LIMA                                   '),
                     ('SANTA CATARINA                                    ',
                      'AMAZONAS                                          ')
                     ]
edgeAlveresCabral = [('ALVARES CABRAL                                    ', 'DO CONTORNO                                       '),
                     ('ALVARES CABRAL                                    ',
                      'DA BAHIA                                          '),
                     ('ALVARES CABRAL                                    ',
                      'AUGUSTO DE LIMA                                   '),
                     ('ALVARES CABRAL                                    ',
                      'AFONSO PENA                                       '),
                     ('ALVARES CABRAL                                    ',
                      'ESPIRITO SANTO                                    '),
                     ('ALVARES CABRAL                                    ', 'CURITIBA                                          ')]

edgeAmazonas = [('AMAZONAS                                          ', 'DO CONTORNO                                       '),
                ('AMAZONAS                                          ',
                 'MATO GROSSO                                       '),
                ('AMAZONAS                                          ',
                 'CURITIBA                                          '),
                ('AMAZONAS                                          ',
                 'AFONSO PENA                                       '),
                ('AMAZONAS                                          ', 'ESPIRITO SANTO                                    ')]

edgeAndradas = [('DOS ANDRADAS                                      ',
                 'DO CONTORNO                                       ')]

edgeAfPena = [('AFONSO PENA                                       ', 'CURITIBA                                          '),
              ('AFONSO PENA                                       ',
               'DO CONTORNO                                       '),
              ('AFONSO PENA                                       ',
               'DA BAHIA                                          '),
              ('AFONSO PENA                                       ',
               'ESPIRITO SANTO                                    '),
              ('AFONSO PENA                                       ', 'CARANDAI                                          ')]

edgeGuaicurus = [('DOS GUAICURUS                                     ', 'CURITIBA                                          '),
                 ('DOS GUAICURUS                                     ', 'DA BAHIA                                          ')]

edgeEspiritoSanto = [('ESPIRITO SANTO                                    ', 'DO CONTORNO                                       '),
                     ('ESPIRITO SANTO                                    ',
                      'BIAS FORTES                                       '),
                     ('ESPIRITO SANTO                                    ', 'AUGUSTO DE LIMA                                   ')]


edgeAugustoLima = [('AUGUSTO DE LIMA                                   ', 'DO CONTORNO                                       '),
                   ('AUGUSTO DE LIMA                                   ',
                    'MATO GROSSO                                       '),
                   ('AUGUSTO DE LIMA                                   ',
                    'CURITIBA                                          '),
                   ('AUGUSTO DE LIMA                                   ', 'DA BAHIA                                          ')]

edgeCuritiba = [('CURITIBA                                          ', 'DO CONTORNO                                       '),
                ('CURITIBA                                          ', 'BIAS FORTES                                       ')]

edgeContorno = [('DO CONTORNO                                       ', 'BIAS FORTES                                       '),
                ('DO CONTORNO                                       ', 'CARANDAI                                          ')]

edgeMGrosso = [('MATO GROSSO                                       ',
                'BIAS FORTES                                       ')]

edgeBiasFortes = [('BIAS FORTES                                       ',
                   'DA BAHIA                                          ')]


aux = dfAcidentes['nome_logradouro'].drop_duplicates('first')
for i in range(aux.size - 1):
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

networkx.draw(graph, with_labels=True,
              node_color = color_map, node_size=800, font_weight='normal')
plt.show()
