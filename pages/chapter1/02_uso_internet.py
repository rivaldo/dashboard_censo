# imports
from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#######################################################################################
register_page(__name__, icon="fa:table", name='02 - Uso da Internet')


##################################### Leitura do dataset ##############################
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)

#####################################################################################
fig01 = go.Figure()

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_APRENDIZAGEM'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Processos de Ensino e Aprendizagem</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))

fig01.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_INTERNET_APRENDIZAGEM'] == 1]['NO_ENTIDADE'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Percentual Ensino e Aprendizagem</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%',
        'valueformat':'.2f'}
    )) 

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_ADMINISTRATIVO'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Uso administrativo</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 

fig01.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_INTERNET_ADMINISTRATIVO'] == 1]['NO_ENTIDADE'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 1], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual Para Uso Administrativo</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%', 'valueformat':'.2f'},
    ))


fig01.update_layout(paper_bgcolor = "lightblue")

######################################################################################


#####################################################################################
layout = html.Div(children=[
    html.Meta(httpEquiv="refresh"),
    html.Br(),
    html.P(
        'Informação Sobre o Uso da Internet nas Escolas',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig01, responsive=True)),
    html.Br(),
]
)