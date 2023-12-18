from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name="04 - Infraestrutura de Rede de Dados")
# Leitura do dataset
dados = pd.read_csv(
    "./assets/data/dados_completos_644_escolas.csv", sep=",", low_memory=False
)
dados.drop(columns="Unnamed: 0", inplace=True)

# Seleção dos dados para criar tabelas de conectividade
dados_conectividade = dados[
    [
        "NU_ANO_CENSO",
        "NO_ENTIDADE",
        "CO_ORGAO_REGIONAL",
        "TP_LOCALIZACAO",
        "IN_LABORATORIO_INFORMATICA",
        "IN_BIBLIOTECA",
        "IN_BIBLIOTECA_SALA_LEITURA",
        "IN_INTERNET",
        "IN_INTERNET_ALUNOS",
        "IN_INTERNET_ADMINISTRATIVO",
        "IN_INTERNET_APRENDIZAGEM",
        "IN_BANDA_LARGA",
        "TP_REDE_LOCAL",
    ]
]

dados_conectividade = dados_conectividade.copy()

# Renomeando os campos para utilizar
dados_conectividade.rename(
    columns={
        "NU_ANO_CENSO": "Ano do Censo",
        "NO_ENTIDADE": "Nome da Escola",
        "CO_ORGAO_REGIONAL": "Gerencia Regional",
        "TP_LOCALIZACAO": "Tipo de Area",
        "IN_LABORATORIO_INFORMATICA": "Laboratorio de informática",
        "IN_BIBLIOTECA": "Biblioteca",
        "IN_BIBLIOTECA_SALA_LEITURA": "Biblioteca ou Sala de Leitura",
        "IN_INTERNET": "Acesso a Internet",
        "IN_INTERNET_ALUNOS": "Internet para Alunos",
        "IN_INTERNET_ADMINISTRATIVO": "Internet para Administração",
        "IN_BANDA_LARGA": "Internet Banda Larga",
        "TP_REDE_LOCAL": "Tipo de Rede Local",
        "IN_INTERNET_APRENDIZAGEM": "Internet para Aprendizagem",
    },
    inplace=True,
)

labels = [
    "Não há rede local interligando computadores",
    "Rede cabeada",
    "Rede sem fio(wi-fi)",
    "Rede cabeada e sem fio(wi-fi)",
]
classes = [0, 1, 2, 3, 9]
rede_local = pd.Series.value_counts(
    pd.cut(
        x=dados_conectividade["Tipo de Rede Local"],
        bins=classes,
        labels=labels,
        include_lowest=True,
    )
)
rede_local = pd.DataFrame(
    {"Tipo de Rede Local": rede_local.index, "Número de escolas": rede_local.array}
)

##########################REDE GERAL###############################################
fig_infra_toda_rede = go.Figure()

fig_infra_toda_rede.add_trace(
    go.Indicator(
        mode="number",
        value=((dados.loc[dados["TP_REDE_LOCAL"] == 0]["NO_ENTIDADE"].count())/\
            dados.shape[0])*100,
        domain={"x": [0, 0.4], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Não Há Infraestrutura de Rede de Dados</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red", }, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)

fig_infra_toda_rede.add_trace(
    go.Indicator(
        mode="number",
        value=((dados.loc[dados["TP_REDE_LOCAL"] == 1]["TP_REDE_LOCAL"].count())/\
            dados.shape[0])*100,
        domain={"x": [0, 0.4], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'><br>Infraestrutura de Rede Cabeada</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red", }, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)
fig_infra_toda_rede.add_trace(
    go.Indicator(
        mode="number",
        value=((dados.loc[dados["TP_REDE_LOCAL"] == 2]["TP_REDE_LOCAL"].count())/\
            (dados.shape[0]))*100,
        domain={"x": [0.8, 1], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Infraestura de Rede WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red", }, 'suffix':'%', 'valueformat':'.0f'},
    )
)
fig_infra_toda_rede.add_trace(
    go.Indicator(
        mode="number",
        value=((dados.loc[dados["TP_REDE_LOCAL"] == 3]["TP_REDE_LOCAL"].count())/\
            dados.shape[0])*100,
        domain={"x": [0.8, 1], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'>Infraestrutura Rede Cabeada e WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
        # The line `"font": {"size": 68, "color": "red"},` is setting the font size to 68 and the
        # font color to red for the number displayed in the indicator.
            "font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)


fig_infra_toda_rede.update_layout(paper_bgcolor="aliceblue")
###############################################################################################
#################### ZONA URBANA ##############################################################
fig_infra_zona_urbana = go.Figure()

fig_infra_zona_urbana.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 0) & (dados['TP_LOCALIZACAO'] == 1)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 1]['NO_ENTIDADE'].count())*100,
        domain={"x": [0, 0.4], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Não Há Infraestrutura de Rede de Dados</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red"},  'suffix':'%', 'valueformat':'.0f'
        },
    )
)

fig_infra_zona_urbana.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 1) & (dados['TP_LOCALIZACAO'] == 1)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 1]['NO_ENTIDADE'].count())*100,
        domain={"x": [0, 0.4], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'><br>Infraestrutura de Rede Cabeada</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={"font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'},
    )
)
fig_infra_zona_urbana.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 2) & (dados['TP_LOCALIZACAO'] == 1)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 1]['NO_ENTIDADE'].count())*100,
        domain={"x": [0.8, 1], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Infraestura de Rede WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"
        },
        number={"font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'},
    )
)
fig_infra_zona_urbana.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 3) & (dados['TP_LOCALIZACAO'] == 1)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 1]['NO_ENTIDADE'].count())*100,
        domain={"x": [0.8, 1], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'>Infraestrutura Rede Cabeada e WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)
fig_infra_zona_urbana.update_layout(paper_bgcolor="aliceblue")
#####################################################################################################
#################################### ZONA RURAL #####################################################
fig_infra_zona_rural = go.Figure()

fig_infra_zona_rural.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 0) & (dados['TP_LOCALIZACAO'] == 2)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 2]['NO_ENTIDADE'].count())*100,
        domain={"x": [0, 0.4], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Não Há Infraestrutura de Rede de Dados</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)

fig_infra_zona_rural.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 1) & (dados['TP_LOCALIZACAO'] == 2)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 2]['NO_ENTIDADE'].count())*100,
        domain={"x": [0, 0.4], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'><br>Infraestrutura de Rede Cabeada</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={"font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'},
    )
)
fig_infra_zona_rural.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 2) & (dados['TP_LOCALIZACAO'] == 2)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 2]['NO_ENTIDADE'].count())*100,
        domain={"x": [0.8, 1], "y": [0.8, 1]},
        title={
            "text": "<span style='font-size:1em'>Infraestura de Rede WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"
        },
        number={"font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'},
    )
)
fig_infra_zona_rural.add_trace(
    go.Indicator(
        mode="number",
        value=(dados.loc[(dados["TP_REDE_LOCAL"] == 3) & (dados['TP_LOCALIZACAO'] == 2)]["NO_ENTIDADE"].count())/\
    (dados.loc[dados['TP_LOCALIZACAO'] == 2]['NO_ENTIDADE'].count())*100,
        domain={"x": [0.8, 1], "y": [0, 0.2]},
        title={
            "text": "<span style='font-size:1em'>Infraestrutura Rede Cabeada e WI-FI</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"
        },
        number={
            "font": {"size": 68, "color": "red"}, 'suffix':'%', 'valueformat':'.0f'
        },
    )
)
fig_infra_zona_rural.update_layout(paper_bgcolor="aliceblue")
##############################################################################################################


layout = html.Div(
    children=[
        html.Meta(httpEquiv="refresh"),
        html.P(
            "Dados Sobre a Infraestrutura de Rede nas Escolas - Geral",
            style={
                "fontSize": 20,
                "color": "white",
                "font-weight": "bold",
                "backgroundColor": "rgb(55, 83, 109)",
                "text-align": "left",
                "padding-left": "10px",
            },
        ),
        html.Div(dcc.Graph(figure=fig_infra_toda_rede)),
        
        html.P(
            "Dados Sobre a Infraestrutura de Rede nas Escolas da Zona Urbana",
            style={
                "fontSize": 20,
                "color": "white",
                "font-weight": "bold",
                "backgroundColor": "rgb(55, 83, 109)",
                "text-align": "left",
                "padding-left": "10px",
            },
        ),
        html.Div(dcc.Graph(figure=fig_infra_zona_urbana)),
        html.P(
            "Dados Sobre a Infraestrutura da Rede de Dados nas Escolas nas Escolas da Zona Rural",
            style={
                "fontSize": 20,
                "color": "white",
                "font-weight": "bold",
                "backgroundColor": "rgb(55, 83, 109)",
                "text-align": "left",
                "padding-left": "10px",
            },
        ),
        html.Div(dcc.Graph(figure=fig_infra_zona_rural)),
    ]
)
