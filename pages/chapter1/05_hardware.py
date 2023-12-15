from dash import dcc, html, Input, Output, callback, register_page, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='05 - Desktops, Notebooks e Tablets')
#Leitura do dataset
dados = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados.drop(columns='Unnamed: 0', inplace=True)

#######################################################################################################################
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)
dados_16_anos = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados_16_anos.drop(columns='Unnamed: 0', inplace=True)
#######################################################################################################################
fig_quantidade_desktops = go.Figure()

fig_quantidade_desktops.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_DESKTOP_ALUNO'] == 1]['IN_DESKTOP_ALUNO'].count(),
    domain = {'x': [0, 0.4], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Computadores Para alunos</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {
        "font":{
            "size":68,
            
            },
        
        },
    )) 
fig_quantidade_desktops.add_trace(go.Indicator(
    mode = "number",
    value =dados['QT_DESKTOP_ALUNO'].sum(),
    domain = {'x': [0.8, 1], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Quantidade Total de Computadores</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}}
    )) 
fig_quantidade_desktops.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_DESKTOP_ALUNO'].sum())/(dados.loc[dados['IN_DESKTOP_ALUNO'] == 1]['IN_DESKTOP_ALUNO'].count()),
    domain = {'x': [0, 0.4], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'><br>Média de Computadores por Escola</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, }, 'valueformat':'.0f'},
    )) 

fig_quantidade_desktops.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_DESKTOP_ALUNO'].sum())/(dados.loc[dados['IN_DESKTOP_ALUNO'] == 1]['QT_MAT_BAS'].sum()),
    domain = {'x': [0.8, 1], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'>Média de Computadores Por Aluno</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}, 'valueformat':'.2f'},    
    ))


fig_quantidade_desktops.update_layout(paper_bgcolor = "aliceblue")
##################################QUANTIDADE NOTEBOOKS#####################################################################################
fig_quantidade_notebooks = go.Figure()

fig_quantidade_notebooks.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_COMP_PORTATIL_ALUNO'] == 1]['IN_COMP_PORTATIL_ALUNO'].count(),
    domain = {'x': [0, 0.4], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Notebooks Para alunos</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68},},
    )) 
fig_quantidade_notebooks.add_trace(go.Indicator(
    mode = "number",
    value =dados['QT_COMP_PORTATIL_ALUNO'].sum(),
    domain = {'x': [0.8, 1], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Quantidade Total de Notebooks</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}}
    )) 
fig_quantidade_notebooks.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_COMP_PORTATIL_ALUNO'].sum())/(dados.loc[dados['IN_COMP_PORTATIL_ALUNO'] == 1]['NO_ENTIDADE'].count()),
    domain = {'x': [0, 0.4], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'><br>Média de Notebooks por Escola</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, }, 'valueformat':'.0f'},
    )) 

fig_quantidade_notebooks.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_COMP_PORTATIL_ALUNO'].sum())/(dados.loc[dados['IN_COMP_PORTATIL_ALUNO'] == 1]['QT_MAT_BAS'].sum()),
    domain = {'x': [0.8, 1], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'>Média de Notebooks Por Aluno</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}, 'valueformat':'.2f'},    
    ))


fig_quantidade_notebooks.update_layout(paper_bgcolor = "aliceblue")
###############################################QUANTIDADE TABLETS####################################################################

fig_quantidade_tablets = go.Figure()

fig_quantidade_tablets.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_TABLET_ALUNO'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.4], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Tablets Para alunos</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68},},
    )) 
fig_quantidade_tablets.add_trace(go.Indicator(
    mode = "number",
    value =dados['QT_TABLET_ALUNO'].sum(),
    domain = {'x': [0.8, 1], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Quantidade Total de Tablets</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}}
    )) 
fig_quantidade_tablets.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_TABLET_ALUNO'].sum())/(dados.loc[dados['IN_TABLET_ALUNO'] == 1]['NO_ENTIDADE'].count()),
    domain = {'x': [0, 0.4], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'><br>Média de Tablets por Escola</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, }, 'valueformat':'.0f'},
    )) 

fig_quantidade_tablets.add_trace(go.Indicator(
    mode = "number",
    value = (dados['QT_TABLET_ALUNO'].sum())/(dados.loc[dados['IN_TABLET_ALUNO'] == 1]['QT_MAT_BAS'].sum()),
    domain = {'x': [0.8, 1], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'>Média de Tablets Por Aluno</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}, 'valueformat':'.2f'},    
    ))


fig_quantidade_tablets.update_layout(paper_bgcolor = "aliceblue")
#########################################################################################################

layout = html.Div(children=[
    html.Meta(httpEquiv="refresh"),
    html.Br(),
    html.P(
        'Informação sobre Desktops para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}
    ),
    html.Div(dcc.Graph(figure=fig_quantidade_desktops, responsive=True)),
    
    html.Br(),
    html.P(
        'Informação sobre Notebooks para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig_quantidade_notebooks, responsive=True)),
    
    html.Br(),
    html.P(
        'Informação sobre Tablets para Uso dos Alunos nas Escolas - Censo 2022',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig_quantidade_tablets, responsive=True))
]
)


