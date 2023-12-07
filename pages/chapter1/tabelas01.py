from dash import dcc, html, Input, Output, callback, register_page, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='01 - Internet - Escolas e Apredizagem')
#Leitura do dataset
dados = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados.drop(columns='Unnamed: 0', inplace=True)

#######################################################################################################################



#######################################################################################################################
layout = html.Div(children=[
    html.Br(),
    html.Div('Tabela 01' ),
    html.Br(),
    html.H3('Tipo de conectividade encontrada nas escolas'),
    dash_table.DataTable(
        id='table',
        data=dados.head().to_dict('records'),
        columns=[{'name': i, 'id':i} for i in dados.columns],
        page_action='none',
        style_table={'height': '300px', 'overflowY': 'auto', },
        style_cell={'textAlign': 'center'},
        style_as_list_view=True,
        style_header={
            'background':'rgb(220, 220, 220)',
            'fontWeight': 'bold'
        }
    ),

    

]
)


