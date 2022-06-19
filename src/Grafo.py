import pandas
from DataFrame import dfAcidentes, dfFiscalizacao
import networkx
import matplotlib.pyplot as plt

graph = networkx.Graph()

nodes = []
edgeTupis = [('DOS TUPIS                                         ','RIO DE JANEIRO                                    '),
             ('DOS TUPIS                                         ','ESPIRITO SANTO                                    '),
             ('DOS TUPIS                                         ','AMAZONAS                                          '),
             ('DOS TUPIS                                         ','CURITIBA                                          '),
             ('DOS TUPIS                                         ','PARANA                                            '),
             ('DOS TUPIS                                         ','DOS GUARANIS                                      '),
             ('DOS TUPIS                                         ','OLEGARIO MACIEL                                   '),
             ('DOS TUPIS                                         ','RIO GRANDE DO SUL                                 '),
             ('DOS TUPIS                                         ','BIAS FORTES                                       '),
             ('DOS TUPIS                                         ','DO CONTORNO                                       '),
             ('DOS TUPIS                                         ','SAO PAULO                                         '),
             ('DOS TUPIS                                         ','DA BAHIA                                          '),
             ('DOS TUPIS                                         ','AFONSO PENA                                       '),
             ('DOS TUPIS                                         ','MATO GROSSO                                       ')]
edgeTimbiras = [('DOS TIMBIRAS                                      ','AFONSO PENA                                       '),
                ('DOS TIMBIRAS                                      ','DA BAHIA                                          '),
                ('DOS TIMBIRAS                                      ','ALVARES CABRAL                                    '),
                ('DOS TIMBIRAS                                      ','ESPIRITO SANTO                                    '),
                ('DOS TIMBIRAS                                      ','RIO DE JANEIRO                                    '),
                ('DOS TIMBIRAS                                      ','SAO PAULO                                         '),
                ('DOS TIMBIRAS                                      ','BIAS FORTES                                       '),
                ('DOS TIMBIRAS                                      ','SANTA CATARINA                                    '),
                ('DOS TIMBIRAS                                      ','OLEGARIO MACIEL                                   '),
                ('DOS TIMBIRAS                                      ','RIO GRANDE DO SUL                                 '),
                ('DOS TIMBIRAS                                      ','AMAZONAS                                          '),
                ('DOS TIMBIRAS                                      ','CURITIBA                                          ')]
edgeTamoios = [('DOS TAMOIOS                                       ','DA BAHIA                                          '),
               ('DOS TAMOIOS                                       ','AFONSO PENA                                       '),
               ('DOS TAMOIOS                                       ','RIO DE JANEIRO                                    '),
               ('DOS TAMOIOS                                       ','AMAZONAS                                          '),
               ('DOS TAMOIOS                                       ','CURITIBA                                          '),
               ('DOS TAMOIOS                                       ','PARANA                                            '),
               ('DOS TAMOIOS                                       ','DOS GUARANIS                                      '),
               ('DOS TAMOIOS                                       ','OLEGARIO MACIEL                                   '),
               ('DOS TAMOIOS                                       ','RIO GRANDE DO SUL                                 '),
               ('DOS TAMOIOS                                       ','MATO GROSSO                                       '),
               ('DOS TAMOIOS                                       ','BIAS FORTES                                       '),
               ('DOS TAMOIOS                                       ','ESPIRITO SANTO                                    '),
               ('DOS TAMOIOS                                       ','SANTA TEREZA                                      '),]
edgeSapucai = [('SAPUCAI                                           ','ASSIS CHATEAUBRIAND                               '),
               ('SAPUCAI                                           ','DO CONTORNO                                       '),]
edgeSaturninhoBrito = [('SATURNINO DE BRITO                                ','SANTOS DUMONT                                     '),
                       ('SATURNINO DE BRITO                                ','VINTE E UM DE ABRIL                               ')]
edgeSaoPaulo = [('SAO PAULO                                         ','DO CONTORNO                                       '),
                ('SAO PAULO                                         ','ALVARES CABRAL                                    '),
                ('SAO PAULO                                         ','BIAS FORTES                                       '),
                ('SAO PAULO                                         ','DOS GUAJAJARAS                                    '),
                ('SAO PAULO                                         ','AUGUSTO DE LIMA                                   '),
                ('SAO PAULO                                         ','DOS GOITACAZES                                    '),
                ('SAO PAULO                                         ','AMAZONAS                                          '),
                ('SAO PAULO                                         ','DOS CARIJOS                                       '),
                ('SAO PAULO                                         ','AFONSO PENA                                       '),
                ('SAO PAULO                                         ','DOS CAETES                                        '),
                ('SAO PAULO                                         ','SANTOS DUMONT                                     '),
                ('SAO PAULO                                         ','DOS GUAICURUS                                     '),
                ('SAO PAULO                                         ','OIAPOQUE                                          ')]
edgeRiobranco = [('RIO BRANCO                                        ','PAULO DE FRONTIN                                  '),
                 ('RIO BRANCO                                        ','SANTOS DUMONT                                     '),
                 ('RIO BRANCO                                        ','DOS CAETES                                        ')]
edgeRioGrandeSul = [('RIO GRANDE DO SUL                                 ','AMAZONAS                                          '),
                    ('RIO GRANDE DO SUL                                 ','DOS GUAJAJARAS                                    '),
                    ('RIO GRANDE DO SUL                                 ','AUGUSTO DE LIMA                                   '),
                    ('RIO GRANDE DO SUL                                 ','DOS GOITACAZES                                    '),
                    ('RIO GRANDE DO SUL                                 ','BIAS FORTES                                       '),
                    ('RIO GRANDE DO SUL                                 ','DOS CARIJOS                                       '),
                    ('RIO GRANDE DO SUL                                 ','DOS TUPINAMBAS                                    '),
                    ('RIO GRANDE DO SUL                                 ','DO CONTORNO                                       ')]
edgeRioJaneiro = [('RIO DE JANEIRO                                    ','DO CONTORNO                                       '),
                  ('RIO DE JANEIRO                                    ','BIAS FORTES                                       '),
                  ('RIO DE JANEIRO                                    ','ALVARES CABRAL                                    '),
                  ('RIO DE JANEIRO                                    ','DOS GUAJAJARAS                                    '),
                  ('RIO DE JANEIRO                                    ','AUGUSTO DE LIMA                                   '),
                  ('RIO DE JANEIRO                                    ','DOS GOITACAZES                                    '),
                  ('RIO DE JANEIRO                                    ','AFONSO PENA                                       '),
                  ('RIO DE JANEIRO                                    ','AMAZONAS                                          '),
                  ('RIO DE JANEIRO                                    ','DOS CARIJOS                                       '),
                  ('RIO DE JANEIRO                                    ','DOS TUPINAMBAS                                    '),
                  ('RIO DE JANEIRO                                    ','DOS CAETES                                        '),
                  ('RIO DE JANEIRO                                    ','SANTOS DUMONT                                     '),
                  ('RIO DE JANEIRO                                    ','DOS GUAICURUS                                     '),
                  ('RIO DE JANEIRO                                    ','OIAPOQUE                                          '),
                  ('RIO DE JANEIRO                                    ','SETE DE SETEMBRO                                  ')]
edgeSantaCatarina = [('SANTA CATARINA                                    ','DO CONTORNO                                       '),
                     ('SANTA CATARINA                                    ','ALVARES CABRAL                                    '),
                     ('SANTA CATARINA                                    ','BIAS FORTES                                       '),
                     ('SANTA CATARINA                                    ','DOS GUAJAJARAS                                    '),
                     ('SANTA CATARINA                                    ','AUGUSTO DE LIMA                                   '),
                     ('SANTA CATARINA                                    ','AMAZONAS                                          '),
                     ('SANTA CATARINA                                    ','DOS GOITACAZES                                    ')]
edgeAlveresCabral = [('ALVARES CABRAL                                    ','DO CONTORNO                                       '),
                     ('ALVARES CABRAL                                    ','OLEGARIO MACIEL                                   '),
                     ('ALVARES CABRAL                                    ','DOS GUAJAJARAS                                    '),
                     ('ALVARES CABRAL                                    ','DA BAHIA                                          '),
                     ('ALVARES CABRAL                                    ','AUGUSTO DE LIMA                                   '),
                     ('ALVARES CABRAL                                    ','AFONSO PENA                                       '),
                     ('ALVARES CABRAL                                    ','ESPIRITO SANTO                                    '),
                     ('ALVARES CABRAL                                    ','CURITIBA                                          '),
                     ('ALVARES CABRAL                                    ','AFONSO ARINOS                                     ')]
edgeAmazonas = [('AMAZONAS                                          ','DO CONTORNO                                       '),
                ('AMAZONAS                                          ','PARANA                                            '),
                ('AMAZONAS                                          ','MATO GROSSO                                       '),
                ('AMAZONAS                                          ','DOS GUAJAJARAS                                    '),
                ('AMAZONAS                                          ','RAUL SOARES                                       '),
                ('AMAZONAS                                          ','DOS GOITACAZES                                    '),
                ('AMAZONAS                                          ','PADRE BELCHIOR                                    '),
                ('AMAZONAS                                          ','CURITIBA                                          '),
                ('AMAZONAS                                          ','AFONSO PENA                                       '),
                ('AMAZONAS                                          ','DOS TUPINAMBAS                                    '),
                ('AMAZONAS                                          ','ESPIRITO SANTO                                    '),
                ('AMAZONAS                                          ','DOS CAETES                                        ')]
edgeAndradas = [('DOS ANDRADAS                                      ','DO CONTORNO                                       '),
              ('DOS ANDRADAS                                      ','RUI BARBOSA                                       '),
              ('DOS ANDRADAS                                      ','DOS CAETES                                        '),
              ('DOS ANDRADAS                                      ','DOS TUPINAMBAS                                    '),
              ('DOS ANDRADAS                                      ','DOS CARIJOS                                       '),
              ('DOS ANDRADAS                                      ','ASSIS CHATEAUBRIAND                               '),
              ('DOS ANDRADAS                                      ','SANTA TEREZA                                      '),
              ('DOS ANDRADAS                                      ','EZEQUIEL DIAS                                     '),
              ('DOS ANDRADAS                                      ','RUI BARBOSA                                       '),
              ('DOS ANDRADAS                                      ','SANTA TEREZA                                      ')]
edgeAfPena = [('AFONSO PENA                                       ','CURITIBA                                          '),
               ('AFONSO PENA                                       ','DO CONTORNO                                       '),
               ('AFONSO PENA                                       ','CARANDAI                                          '),
               ('AFONSO PENA                                       ','DOS GUAJAJARAS                                    '),
               ('AFONSO PENA                                       ','DA BAHIA                                          '),
               ('AFONSO PENA                                       ','ESPIRITO SANTO                                    '),
               ('AFONSO PENA                                       ','DOS CARIJOS                                       '),
               ('AFONSO PENA                                       ','DOS TUPINAMBAS                                    '),
               ('AFONSO PENA                                       ','DOS CAETES                                        ')]
edgeCarijos = [('DOS CARIJOS                                       ','DO CONTORNO                                       '),
               ('DOS CARIJOS                                       ','OLEGARIO MACIEL                                   '),
               ('DOS CARIJOS                                       ','DOS GUARANIS                                      '),
               ('DOS CARIJOS                                       ','PARANA                                            '),
               ('DOS CARIJOS                                       ','CURITIBA                                          '),
               ('DOS CARIJOS                                       ','ESPIRITO SANTO                                    '),
               ('DOS CARIJOS                                       ','DA BAHIA                                          '),
               ('DOS CARIJOS                                       ','SETE DE SETEMBRO                                  ')]
edgeGuaicurus = [('DOS GUAICURUS                                     ','CURITIBA                                          '),
                 ('DOS GUAICURUS                                     ','ESPIRITO SANTO                                    '),
                 ('DOS GUAICURUS                                     ','DA BAHIA                                          '),
                 ('DOS GUAICURUS                                     ','VINTE E UM DE ABRIL                               ')]
edgeGuaranis = [('DOS GUARANIS                                      ','DOS TUPINAMBAS                                    '),
                ('DOS GUARANIS                                      ','DOS CAETES                                        '),
                ('DOS GUARANIS                                      ','PAULO DE FRONTIN                                  ')]
edgeEzequiel = [('EZEQUIEL DIAS                                     ','CARANDAI                                          ')]
edgeEspiritoSanto = [('ESPIRITO SANTO                                    ','DO CONTORNO                                       '),
                     ('ESPIRITO SANTO                                    ','BIAS FORTES                                       '),
                     ('ESPIRITO SANTO                                    ','DOS GUAJAJARAS                                    '),
                     ('ESPIRITO SANTO                                    ','AUGUSTO DE LIMA                                   '),
                     ('ESPIRITO SANTO                                    ','DOS GOITACAZES                                    '),
                     ('ESPIRITO SANTO                                    ','DOS TUPINAMBAS                                    '),
                     ('ESPIRITO SANTO                                    ','DOS CAETES                                        '),
                     ('ESPIRITO SANTO                                    ','SANTOS DUMONT                                     ')
                     ]
edgeAfArinos = [('AFONSO ARINOS                                     ','AUGUSTO DE LIMA                                   ')]
edgeAugustoLima = [('AUGUSTO DE LIMA                                   ','DO CONTORNO                                       '),
                   ('AUGUSTO DE LIMA                                   ','MATO GROSSO                                       '),
                   ('AUGUSTO DE LIMA                                   ','CURITIBA                                          '),
                   ('AUGUSTO DE LIMA                                   ','PADRE BELCHIOR                                    '),
                   ('AUGUSTO DE LIMA                                   ','DA BAHIA                                          '),
                   ('AUGUSTO DE LIMA                                   ','DOS CAETES                                        ')]
edgeCuritiba = [('CURITIBA                                          ','DO CONTORNO                                       '),
                ('CURITIBA                                          ','PADRE BELCHIOR                                    '),
                ('CURITIBA                                          ','BIAS FORTES                                       '),
                ('CURITIBA                                          ','DOS GUAJAJARAS                                    '),
                ('CURITIBA                                          ','DOS GOITACAZES                                    '),
                ('CURITIBA                                          ','DOS TUPINAMBAS                                    '),
                ('CURITIBA                                          ','SANTOS DUMONT                                     '),
                ('CURITIBA                                          ','OIAPOQUE                                          ')]
edgeContorno = [('DO CONTORNO                                       ','CARANDAI                                          '),
                ('DO CONTORNO                                       ','DOS TUPINAMBAS                                    '),
                ('DO CONTORNO                                       ','DOS CAETES                                        '),
                ('DO CONTORNO                                       ','DOS GUAJAJARAS                                    '),
                ('DO CONTORNO                                       ','PAULO DE FRONTIN                                  '),
                ('DO CONTORNO                                       ','VINTE E UM DE ABRIL                               '),
                ('DO CONTORNO                                       ','OIAPOQUE                                          '),
                ('DO CONTORNO                                       ','SARAH KUBITSCHEK                                  '),
                ('DO CONTORNO                                       ','VARGINHA                                          '),
                ('DO CONTORNO                                       ','BIAS FORTES                                       '),
                ('DO CONTORNO                                       ','DOS GOITACAZES                                    '),
                ('DO CONTORNO                                       ','DONA MARGARIDA GENARO                             '),]
edgeBelchior = [('PADRE BELCHIOR                                    ','DOS GOITACAZES                                    ')]
edgeParana = [('PARANA                                            ','PAULO DE FRONTIN                                  '),
              ('PARANA                                            ','DOS CAETES                                        '),
              ('PARANA                                            ','DOS TUPINAMBAS                                    '),]
edgeMaciel = [('OLEGARIO MACIEL                                   ','PAULO DE FRONTIN                                  '),
              ('OLEGARIO MACIEL                                   ','DOS CAETES                                        '),
              ('OLEGARIO MACIEL                                   ','DOS TUPINAMBAS                                    '),
              ('OLEGARIO MACIEL                                   ','DOS GOITACAZES                                    '),
              ('OLEGARIO MACIEL                                   ','RAUL SOARES                                       '),
              ('OLEGARIO MACIEL                                   ','DOS GUAJAJARAS                                    '),]
edgeOiapoque = [('OIAPOQUE                                          ','VINTE E UM DE ABRIL                               ')]
edgeCaetes = [('DOS CAETES                                        ','DA BAHIA                                          '),
              ('DOS CAETES                                        ','SARAH KUBITSCHEK                                  ')]
edgeMGrosso = [('MATO GROSSO                                       ','BIAS FORTES                                       '),
               ('MATO GROSSO                                       ','DOS GOITACAZES                                    '),
               ('MATO GROSSO                                       ','DOS GUAJAJARAS                                    '),]
edgeLeviCoelho = [('LEVI COELHO DA ROCHA                              ','DOS GUAJAJARAS                                    ')]
edgeAssis=[('ASSIS CHATEAUBRIAND                               ','DA BAHIA                                          ')]
edgeRaulSoares=[('RAUL SOARES                                       ','BIAS FORTES                                       ')]
edgeRuiBarbosa=[('RUI BARBOSA                                       ','DA BAHIA                                          ')]
edgeSantosDumont=[('SANTOS DUMONT                                     ','DA BAHIA                                          ')]
edgeSarahKubitschek = [('SARAH KUBITSCHEK                                  ','PAULO DE FRONTIN                                  ')]
edgeBiasFortes = [('BIAS FORTES                                       ','DOS GOITACAZES                                    '),('BIAS FORTES                                       ','DOS GUAJAJARAS                                    '),('BIAS FORTES                                       ','DA BAHIA                                          ')]
edgeGoitacazes = [('DOS GOITACAZES                                    ','DA BAHIA                                          ')]
edgeGuajajaras = [('DOS GUAJAJARAS                                    ','DA BAHIA                                          ')]
edgeTupinambas = [('DOS TUPINAMBAS                                    ','DA BAHIA                                          ')]



nodes = dfAcidentes['nome_logradouro'].drop_duplicates('first')
graph.add_nodes_from(nodes)
graph.add_edges_from(edgeTupis)
graph.add_edges_from(edgeTimbiras)
graph.add_edges_from(edgeTamoios)
graph.add_edges_from(edgeSapucai)
graph.add_edges_from(edgeSaturninhoBrito)
graph.add_edges_from(edgeSaoPaulo)
graph.add_edges_from(edgeRiobranco)
graph.add_edges_from(edgeRioGrandeSul)
graph.add_edges_from(edgeRioJaneiro)
graph.add_edges_from(edgeSantaCatarina)
graph.add_edges_from(edgeAlveresCabral)
graph.add_edges_from(edgeAmazonas)
graph.add_edges_from(edgeAndradas)
graph.add_edges_from(edgeAfPena)
graph.add_edges_from(edgeCarijos)
graph.add_edges_from(edgeGuaicurus)
graph.add_edges_from(edgeGuaranis)
graph.add_edges_from(edgeEzequiel)
graph.add_edges_from(edgeEspiritoSanto)
graph.add_edges_from(edgeAfArinos)
graph.add_edges_from(edgeAugustoLima)
graph.add_edges_from(edgeCuritiba)
graph.add_edges_from(edgeContorno)
graph.add_edges_from(edgeBelchior)
graph.add_edges_from(edgeParana)
graph.add_edges_from(edgeMaciel)
graph.add_edges_from(edgeOiapoque)
graph.add_edges_from(edgeCaetes)
graph.add_edges_from(edgeMGrosso)
graph.add_edges_from(edgeLeviCoelho)
graph.add_edges_from(edgeAssis)
graph.add_edges_from(edgeRaulSoares)
graph.add_edges_from(edgeRuiBarbosa)
graph.add_edges_from(edgeSantosDumont)
graph.add_edges_from(edgeSarahKubitschek)
graph.add_edges_from(edgeBiasFortes)
graph.add_edges_from(edgeGoitacazes)
graph.add_edges_from(edgeGuajajaras)
graph.add_edges_from(edgeTupinambas)                   

networkx.draw(graph, with_labels=True, font_weight='normal')
plt.show()
