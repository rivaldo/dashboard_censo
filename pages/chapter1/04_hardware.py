from dash import dcc, html, Input, Output, callback, register_page, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='04 - Desktops, Notebooks e Tablets')
#Leitura do dataset
dados = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados.drop(columns='Unnamed: 0', inplace=True)

#######################################################################################################################

dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)
dados_16_anos = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados_16_anos.drop(columns='Unnamed: 0', inplace=True)
#######################################################################################################################
fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_DESKTOP_ALUNO'] == 1]['IN_DESKTOP_ALUNO'].count(),
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número De Escolas Com Desktops Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))


fig.add_trace(go.Indicator(
    mode = "number",
    value = dados['QT_DESKTOP_ALUNO'].sum(),
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número de desktops Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}}
    )) 

fig.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_DESKTOP_ALUNO'] == 1]['IN_DESKTOP_ALUNO'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%', 'valueformat':'.2f'},
    ))
fig.update_layout(paper_bgcolor = "lightblue")
#######################################################################################################################
fig01 = go.Figure()

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_COMP_PORTATIL_ALUNO'] == 1]['IN_DESKTOP_ALUNO'].count(),
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número De Escolas Com Notebooks Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))


fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados['QT_COMP_PORTATIL_ALUNO'].sum(),
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número de Notebooks Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}}
    )) 

fig01.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_COMP_PORTATIL_ALUNO'] == 1]['IN_COMP_PORTATIL_ALUNO'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}, 'suffix':'%', 'valueformat':'.2f'},
    ))
fig01.update_layout(paper_bgcolor = "lightblue")
###################################################################################################################

fig02 = go.Figure()

fig02.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_TABLET_ALUNO'] == 1]['IN_TABLET_ALUNO'].count(),
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número De Escolas Com Desktops Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))


fig02.add_trace(go.Indicator(
    mode = "number",
    value = dados['QT_TABLET_ALUNO'].sum(),
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número de desktops Para Uso dos Alunos</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}}
    )) 

fig02.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_TABLET_ALUNO'] == 1]['IN_TABLET_ALUNO'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}, 'suffix':'%', 'valueformat':'.2f'},
    ))
fig02.update_layout(paper_bgcolor = "lightblue")
#########################################################################################################

layout = html.Div(children=[
    html.Br(),
    html.P(
        'Informação sobre Desktops para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}
    ),
    html.Div(dcc.Graph(figure=fig, responsive=True)),
    
    html.Br(),
    html.P(
        'Informação sobre Notebooks para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig01, responsive=True)),
    
    html.Br(),
    html.P(
        'Informação sobre Tablets para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig02, responsive=True))
]
)


