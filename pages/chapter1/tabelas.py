from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table")
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
]]

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

#Verificar os numeros das escolas que possuem conecvidade
frequencia_internet = dados_conectividade['Acesso a Internet'].value_counts()
percentual_internet = dados_conectividade['Acesso a Internet'].value_counts(normalize=True).round(3)*100
escolas_com_internet = pd.DataFrame({'Número de Escolas da Rede Estadual com Internet':frequencia_internet, 'Percentual das Escolas da Rede Estadual com Internet (%)':percentual_internet})
escolas_com_internet.rename(index={0.0:'Não possui acesso', 1.0:'Possui acesso'}, inplace=True)
escolas_com_internet.rename_axis('A escola possui acesso a internet ?', inplace=True)
escolas_com_internet


layout = html.Div([
    html.P('Teste')
]
)

