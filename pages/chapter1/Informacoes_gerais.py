# imports
from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#######################################################################################
register_page(__name__, icon="fa:table", name='Números da Rede Estadual')
#Leitura do dataset
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)



fig01 = go.Figure()
fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.shape[0],
    title = {'text':'Número de Escolas Estaduais <br>'
            "<span style='font-size:0.6em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    
    domain = {'x': [0.25, 0.75], 'y': [0.5, 1.0]}
    ))

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count(),
    title = {'text':'Número de escolas Com Acesso a Internet <br>'
            "<span style='font-size:0.6em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>" },
    number = {"font":{"size":68}},
    domain = {'x': [0.25, 0.75], 'y': [0.0, 0.4]}
    ))
fig01.update_layout(paper_bgcolor = "lightblue")
#####################################################################################

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.shape[0],
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número de Escolas Estaduais</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 

fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_APRENDIZAGEM'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Escolas Com Internet Para Aprendizagem</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 
fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Internet</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}}
    )) 
fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_ALUNOS'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0.5, 1], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Escolas com Internet Para Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))


fig.update_layout(paper_bgcolor = "lightblue")




#####################################################################################
layout = html.Div(children=[
    
    html.Br(),
    html.Div(dcc.Graph(figure=fig, responsive=True)),
    html.Br(),
]
)