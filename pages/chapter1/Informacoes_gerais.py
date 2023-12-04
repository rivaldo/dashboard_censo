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

fig = go.Figure()
fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.shape[0],
    title = {'text':'Número de escolas Estaduais <br>'
            "<span style='font-size:0.8em;color:gray'>Microdados - Cernso 2022</span>" +
            "<br><span style='font-size:0.8em;color:gray'>fonte: INEP</span>"},
    domain = {'x': [0.25, 0.75], 'y': [0.5, 1.0]}
    ))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count(),
    delta = {'reference': dados.shape[0], 'relative': False,
            'position' : "right", "valueformat": "0.0f", 'suffix':' Número de Escolas Sem Internet'},
    title = {'text': "Total de Escolas com Internet", 'font': {'size': 24}},
    domain = {'x': [0.25, 0.75], 'y': [0.0, 0.4]}
    ))
fig.update_layout(paper_bgcolor = "lightblue")

fig01 = go.Figure()
fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.shape[0],
    title = {'text':'Número de escolas Estaduais <br>'
            "<span style='font-size:0.8em;color:gray'>Microdados - Cernso 2022</span>" +
            "<br><span style='font-size:0.8em;color:gray'>fonte: INEP</span>"},
    domain = {'x': [0.25, 0.75], 'y': [0.5, 1.0]}
    ))

fig01.add_trace(go.Indicator(
    mode = "number+delta",
    value = dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count(),
    delta = {'reference': dados.shape[0], 'relative': False,
            'position' : "right", "valueformat": "0.0f", 'suffix':' Número de Escolas Sem Internet'},
    title = {'text': "Total de Escolas com Internet", 'font': {'size': 24}},
    domain = {'x': [0.25, 0.75], 'y': [0.0, 0.4]}
    ))
fig01.update_layout(paper_bgcolor = "lightblue")




layout = html.Div(children=[
    html.Br(),
    #html.Div(dcc.Graph(figure=fig_numero_de_escolas, responsive=True), ),
    html.Br(),
    html.Div(dcc.Graph(figure=fig, responsive=True), ),
    html.Br(),
    html.Div(dcc.Graph(figure=fig01, responsive=True)),
    html.Br(),
]
)