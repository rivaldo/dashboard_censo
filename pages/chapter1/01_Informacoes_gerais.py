# imports
from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#######################################################################################
register_page(__name__, icon="fa:table", name='01 - Rede Estadual')
#Leitura do dataset
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)
dados_16_anos = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados_16_anos.drop(columns='Unnamed: 0', inplace=True)
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
    value = ((dados.shape[0])/(dados_16_anos.loc[dados_16_anos['NU_ANO_CENSO'] == 2007])['NO_ENTIDADE'].count())*100,
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Redução da Rede Escolar de 2007 a 2022</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"prefix":"&#129047;","font":{"size":68, 'color':'red'}, 'suffix':'%',
        'valueformat':'.2f', }
    )) 

fig.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Escolas Com Internet</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 

fig.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_INTERNET'] == 1]['NO_ENTIDADE'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 1], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas com Internet</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%', 'valueformat':'.2f'},
    ))


fig.update_layout(paper_bgcolor = "aliceblue")
######################### APRENDIZAGEM E ADMINISTRATIVO ###########################################################

fig01 = go.Figure()

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_APRENDIZAGEM'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Internet - Usada nos processos de ensino e aprendizagem</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    ))

fig01.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[dados['IN_INTERNET_APRENDIZAGEM'] == 1]['NO_ENTIDADE'].count())/(dados.shape[0]))*100,
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Percentual para Uso no Ensino e Aprendizagem</span><br>"
            "<span style='font-size:0.4em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%',
        'valueformat':'.2f'}
    )) 

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_INTERNET_ADMINISTRATIVO'] == 1]['NO_ENTIDADE'].count(),
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Acesso à Internet - Para uso administrativo</span><br>"
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


fig01.update_layout(paper_bgcolor = "aliceblue")

############################# ZONA RURAL #######################################################
fig_zona_rural = go.Figure()

fig_zona_rural.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['TP_LOCALIZACAO'] ==2)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0, 0.4], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Número de Escolas da Zona Rural</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {
        "font":{
            "size":68,
            
            },
        
        },
    )) 
fig_zona_rural.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['IN_INTERNET'] == 1) & (dados['TP_LOCALIZACAO'] ==2)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0.8, 1], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Internet </span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}}
    )) 
fig_zona_rural.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['IN_INTERNET'] == 0) & (dados['TP_LOCALIZACAO'] ==2)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0, 0.4], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'><br>Escolas Sem Internet </span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}},
    )) 

fig_zona_rural.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[(dados['IN_INTERNET'] == 1) & (dados['TP_LOCALIZACAO'] ==2)]['TP_LOCALIZACAO'].count())\
            /(dados.loc[(dados['TP_LOCALIZACAO'] ==2)]['TP_LOCALIZACAO'].count()))*100,
    domain = {'x': [0.8, 1], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas com Internet</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%', 'valueformat':'.2f'},    
    ))


fig_zona_rural.update_layout(paper_bgcolor = "aliceblue")

################################# ZONA URBANA #######################################

fig_zona_urbana = go.Figure()

fig_zona_urbana.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['TP_LOCALIZACAO'] ==1)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0, 0.4], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas da Zona Urbana</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {
        "font":{
            "size":68,
            
            },
        
        },
    )) 
fig_zona_urbana.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['IN_INTERNET'] == 1) & (dados['TP_LOCALIZACAO'] ==1)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0.8, 1], 'y': [0.8, 1]},
    title = {"text": "<span style='font-size:1em'>Escolas com Internet </span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}}
    )) 
fig_zona_urbana.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['IN_INTERNET'] == 0) & (dados['TP_LOCALIZACAO'] ==1)]['TP_LOCALIZACAO'].count(),
    domain = {'x': [0, 0.4], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'><br>Escolas Sem Internet </span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'red'}},
    )) 

fig_zona_urbana.add_trace(go.Indicator(
    mode = "number",
    value = ((dados.loc[(dados['IN_INTERNET'] == 1) & (dados['TP_LOCALIZACAO'] ==1)]['TP_LOCALIZACAO'].count())\
             /(dados.loc[(dados['TP_LOCALIZACAO'] ==1)]['TP_LOCALIZACAO'].count()))*100,
    domain = {'x': [0.8, 1], 'y': [0, 0.2]},
    title = {"text": "<span style='font-size:1em'>Percentual das Escolas com Internet</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68, 'color':'green'}, 'suffix':'%', 'valueformat':'.2f'},    
    ))


fig_zona_urbana.update_layout(paper_bgcolor = "aliceblue")

#####################################################################################
layout = html.Div(children=[
    html.Meta(httpEquiv="refresh"),
    html.Br(),
    html.P(
        'Internet na Rede Estadual',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig, responsive=True)),
    html.Br(),
    html.Br(),
    html.P(
        'Internet nas Escolas da Zona Urbana',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig_zona_urbana, responsive=True)),
    html.Br(),
    html.P(
        'Internet nas Escolas da Zona Rural',
        style={'fontSize':20, 'color':'white', "font-weight": "bold", 'backgroundColor':'rgb(55, 83, 109)', 'text-align':'left', 'padding-left':'10px'}        
        ),
    html.Div(dcc.Graph(figure=fig_zona_rural, responsive=True)),
    html.Br(),
]
)