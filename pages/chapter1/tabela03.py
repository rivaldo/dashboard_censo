from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='Tipo de Interligação de Rede nas Escolas')
#Leitura do dataset
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False)
dados.drop(columns='Unnamed: 0', inplace=True)

#Seleção dos dados para criar tabelas de conectividade
dados_conectividade = dados[[
    'NU_ANO_CENSO', 'NO_ENTIDADE', 'CO_ORGAO_REGIONAL',
    'TP_LOCALIZACAO', 'IN_LABORATORIO_INFORMATICA', 
    'IN_BIBLIOTECA', 'IN_BIBLIOTECA_SALA_LEITURA', 
    'IN_INTERNET', 'IN_INTERNET_ALUNOS', 
    'IN_INTERNET_ADMINISTRATIVO', 'IN_INTERNET_APRENDIZAGEM',
    'IN_BANDA_LARGA','TP_REDE_LOCAL'
]].copy()

#Renomeando os campos para utilizar
dados_conectividade.rename(columns={
    'NU_ANO_CENSO':'Ano do Censo', 'NO_ENTIDADE':'Nome da Escola','CO_ORGAO_REGIONAL':'Gerencia Regional' ,
    'TP_LOCALIZACAO':'Tipo de Area', 'IN_LABORATORIO_INFORMATICA':'Laboratorio de informática', 
    'IN_BIBLIOTECA': 'Biblioteca', 'IN_BIBLIOTECA_SALA_LEITURA':'Biblioteca ou Sala de Leitura', 
    'IN_INTERNET':'Acesso a Internet', 'IN_INTERNET_ALUNOS':'Internet para Alunos', 
    'IN_INTERNET_ADMINISTRATIVO':'Internet para Administração', 'IN_BANDA_LARGA':'Internet Banda Larga',
    'TP_REDE_LOCAL': 'Tipo de Rede Local', 'IN_INTERNET_APRENDIZAGEM':'Internet para Aprendizagem'
    },
    inplace=True
)

labels = ['Não', 'Sim']
classes = [-1, 0, 1]

escolas_com_internet = pd.Series.value_counts(
    pd.cut(
        x = dados_conectividade['Acesso a Internet'],
        bins = classes,
        labels=labels,
        include_lowest=True
    )
)
escolas_com_internet_percentual = pd.Series.value_counts(
    pd.cut(
        x = dados_conectividade['Acesso a Internet'],
        bins = classes,
        labels=labels,
        include_lowest=True
    ),
    normalize=True
).round(3)*100

escolas_com_internet_dataframe = pd.DataFrame({
    'A escola possui acesso a internet ?':escolas_com_internet.index,
    'Número de Escolas da Rede Estadual com Internet':escolas_com_internet.array,
    'Percentual das Escolas da Rede Estadual com Internet (%)':escolas_com_internet_percentual.array
    
    
})
layout = html.Div(
    children=[
        html.H1('Informação sobre conectividade'),
        
        html.Div(
            dash_table.DataTable(
            id='table',
            data=escolas_com_internet_dataframe.to_dict('records'),
            columns=[{'name': i, 'id':i} for i in escolas_com_internet_dataframe.columns],
            page_action='none',
            style_table={'height': '750px', 'overflowY': 'auto', },
            style_cell={'textAlign': 'center'},
            style_as_list_view=False,
            style_header={
                'background':'rgb(220, 220, 220)',
                'fontWeight': 'bold'
            }
            )
        ),
        
    ]
)