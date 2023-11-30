from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='Internet - Escolas e Apredizagem')
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
######  FIG01 #################################################################################################
#Verificar os numeros das escolas que possuem conecvidade
frequencia_internet = dados_conectividade['Acesso a Internet'].value_counts()
percentual_internet = dados_conectividade['Acesso a Internet'].value_counts(normalize=True).round(3)*100
escolas_com_internet = pd.DataFrame({'Número de Escolas da Rede Estadual com Internet':frequencia_internet, 'Percentual das Escolas da Rede Estadual com Internet (%)':percentual_internet})
escolas_com_internet.rename(index={0.0:'Não possui acesso', 1.0:'Possui acesso'}, inplace=True)
escolas_com_internet.rename_axis('A escola possui acesso a internet ?', inplace=True)
escolas_com_internet

#Criar Tabela das Escolas que possuem acesso a internet
headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

fig01 = go.Figure(data=[go.Table(
header=dict(
    values=['<b>A escola possui acesso a internet ?</b>','<b>Quantidade de escolas</b>','<b>Percentual das escolas</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['center','center'],
    font=dict(color='white', size=12)
),
cells=dict(
    values=[
    ['Sim', 'Não'],
    [
        escolas_com_internet['Número de Escolas da Rede Estadual com Internet'].iloc[0], 
        escolas_com_internet['Número de Escolas da Rede Estadual com Internet'].iloc[1], 
    ],
    [
        f"{escolas_com_internet['Percentual das Escolas da Rede Estadual com Internet (%)'].iloc[0].round(3)}%", 
        f'{escolas_com_internet["Percentual das Escolas da Rede Estadual com Internet (%)"].iloc[1].round(3)}%', 
    ],
],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor ]*2],
    align = ['center', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])
annotations = [
    dict(
        xref='paper',
        yref='paper',
        x=0.5,
        y=0.7,
        xanchor='center',
        yanchor='top',
        text='Fonte: INEP - ' + 'Microdados Censo 2022',
        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
        showarrow=False,
    )
]
fig01.update_layout(
    title='<b>Escolas com Acesso a Internet - Microdados Censo 2022</b>',
    title_font_color='black',
    annotations = annotations,
    width = 100,
    height = 100
)
################################### FIG02 ######################
################################################################
frequencia_internet_aprendizagem = dados_conectividade['Internet para Aprendizagem'].value_counts()
percentual_internet_aprendizagem = dados_conectividade['Internet para Aprendizagem'].value_counts(normalize=True).round(3)*100
escolas_com_internet_aprendizagem = pd.DataFrame({
    'Número de Escolas com Internet para uso na aprendizagem':frequencia_internet_aprendizagem, 
    'Percentual das Escolas com Internet para uso na aprendizagem (%)':percentual_internet_aprendizagem})
escolas_com_internet_aprendizagem.rename(index={0.0:'Não', 1.0:'Sim'}, inplace=True)
escolas_com_internet_aprendizagem.rename_axis('A escola possui acesso a internet para uso nos processos de aprendizagem ?', inplace=True)
escolas_com_internet_aprendizagem

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

fig02 = go.Figure(data=[go.Table(
header=dict(
    values=['<b>A escola possui acesso a internet para uso nos processos de aprendizagem ?</b>','<b>Quantidade de escolas</b>','<b>Percentual das escolas</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['center','center'],
    font=dict(color='white', size=12)
),
cells=dict(
    values=[
        ['Sim', 'Não'],
        [
            escolas_com_internet_aprendizagem['Número de Escolas com Internet para uso na aprendizagem'].iloc[0], 
            escolas_com_internet_aprendizagem['Número de Escolas com Internet para uso na aprendizagem'].iloc[1], 
        ],
        [
            f"{escolas_com_internet_aprendizagem['Percentual das Escolas com Internet para uso na aprendizagem (%)'].iloc[0].round(3)}%", 
            f'{escolas_com_internet_aprendizagem["Percentual das Escolas com Internet para uso na aprendizagem (%)"].iloc[1].round(3)}%', 
        ],
],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor]],
    align = ['center', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])
annotations = [
    dict(
        xref='paper',
        yref='paper',
        x=0.5,
        y=0.6,
        xanchor='center',
        yanchor='top',
        text='Fonte: INEP - ' + 'Microdados Censo 2022',
        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
        showarrow=False,
    )
]
fig02.update_layout(
    title='<b>Escolas com Internet Para Uso na Aprendizagem - Microdados Censo 2022</b>',
    title_font_color='black',
    annotations=annotations
)




layout = html.Div(children=[
    html.Br(),
    html.Div(dcc.Graph(figure=fig01, responsive=True), ),
    html.Br(),
    html.Div(dcc.Graph(figure=fig02, responsive=True)),
    html.Br(),
    

],
#style={'display':'compact'}
)


