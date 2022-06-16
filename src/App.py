from xml.etree.ElementTree import TreeBuilder
import pandas
import networkx
import matplotlib.pyplot as plt

pathAcidentes = r"dados\acidentes_si-log-2020.csv"
pathFiscalizacao = r"dados\fiscalizacao_eletronica_jan2021.csv"
dfAcidentes = pandas.read_csv(pathAcidentes, encoding='unicode_escape')
dfFiscalizacao = pandas.read_csv(pathFiscalizacao)

# sdfAcidentes = dfAcidentes[].str.split(";")

dfAcidentes[[
    'Nº_boletim',
    'data_boletim',
    'Nº_municipio',
    'nome_municipio',
    'seq_logradouros',
    'Nº_logradouro',
    'tipo_logradouro',
    'nome_logradouro',
    'tipo_logradouro_anterior',
    'nome_logradouro_anterior',
    'Nº_bairro',
    'nome_bairro',
    'tipo_bairro',
    'descricao_tipo_bairro',
    'Nº_imovel',
    'Nº_imovel_proximo'
]] = dfAcidentes[
    'Nº_boletim;data_boletim; Nº_municipio;nome_municipio;seq_logradouros;Nº_logradouro;tipo_logradouro;nome_logradouro;tipo_logradouro_anterior;nome_logradouro_anterior;Nº_bairro;nome_bairro;tipo_bairro;descricao_tipo_bairro;Nº_imovel;Nº_imovel_proximo'
].str.split(';', expand=True)

dfAcidentes = dfAcidentes[[
    "Nº_logradouro",
    "tipo_logradouro",
    "nome_logradouro",
    "Nº_bairro",
    "nome_bairro",
    "Nº_imovel"
]]

coreu = "CORACAO EUCARISTICO"
dfAcidentes = dfAcidentes[dfAcidentes['nome_bairro'].str.contains(coreu)]

dfFiscalizacao = dfFiscalizacao[[
    "ID_FISCALIZACAO_ELETRONICA",
    "DESC_LOC_CONTROLADOR_TRANSITO",
    "DESC_TIPO_CONTROLADOR_TRANSITO",
    "SENTIDO",
    "SENTIDO_FISCALIZADO",
    "GEOMETRIA"
]]
var = 0
teste = []
aux = []
anterior = ""

while (var < dfAcidentes['nome_logradouro'].size):
    nomeRua = dfAcidentes['nome_logradouro'].iloc[var].replace(" ", "")
    if (nomeRua == anterior):
        var += 1
        continue
    nomeRua, " = ", dfFiscalizacao[dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper(
    ).str.replace(" ", "").str.contains(nomeRua)]
    anterior = nomeRua
    for i in range(dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].size - 1):
        if (dfFiscalizacao['DESC_LOC_CONTROLADOR_TRANSITO'].str.upper(
        ).str.replace(" ", "").str.contains(nomeRua).iloc[i]):
            aux.append(dfFiscalizacao.iloc[i])
    var += 1

dfFiscalizacao = pandas.DataFrame(aux)


# graph = networkx.Graph()
# graph.add_ Nºde(1)
# graph.add_ Nºdes_from([
#     (2, {"color": "red"}),
#     (3, {"color": "green"})
# ])
# graph.add_edge(1, 2)
# graph.add_edges_from([(2, 3), (3, 4)])
#  Nºde_list = graph. Nºdes()

# graph[1]

# networkx.draw(graph, with_labels=True, font_weight='bold')
# plt.show()
