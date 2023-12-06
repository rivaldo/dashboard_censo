from dash import dcc, html, Input, Output, callback, register_page, Dash, dash_table
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objects as go

register_page(__name__, icon="fa:table", name='03 - Escolas Técnicas')
#Leitura do dataset
dados = pd.read_csv('./assets/data/dados_completos_644_escolas.csv', sep=',', low_memory=False, encoding='latin-1')
dados.drop(columns='Unnamed: 0', inplace=True)
dados_16_anos = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1')
dados_16_anos.drop(columns='Unnamed: 0', inplace=True)

escolas_profissionalizantes_16_anos = dados_16_anos.groupby('NU_ANO_CENSO')[['IN_PROF']].sum()
escolas_profissionalizantes_16_anos.rename(columns={'IN_PROF':'Número de Escolas Técnicas'}, inplace=True)
escolas_profissionalizantes_16_anos.rename_axis('Ano do Censo', inplace=True)

df_escolas_profissionalizantes_16_anos = pd.DataFrame({
    'Ano do Censo': escolas_profissionalizantes_16_anos.index,
    'Número de Escolas Profissionalizantes': escolas_profissionalizantes_16_anos['Número de Escolas Técnicas'].array
})
df_escolas_profissionalizantes_16_anos.rename_axis('', inplace=True)
df_escolas_profissionalizantes_16_anos.reset_index(drop=True, inplace=True)

years = [ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
########GRAFICO EVOLUÇÃO DOS ECITS##################
fig = go.Figure()
fig.add_trace(go.Bar(x=df_escolas_profissionalizantes_16_anos['Ano do Censo'],
                y=df_escolas_profissionalizantes_16_anos['Número de Escolas Profissionalizantes'],
                name='Número de escolas',
                marker_color='rgb(55, 83, 109)', 
                text=df_escolas_profissionalizantes_16_anos['Número de Escolas Profissionalizantes'],
                ))
fig.update_xaxes(dtick=[ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
fig.update_layout(
    title='Evolução das Escolas Técnicas Estaduais de 2007 a 2022',
    title_font_size=22,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Número de Escolas',
        titlefont_size=18,
        tickfont_size=12,
    ),
    xaxis=dict(
        title='Ano do Censo',
        titlefont_size=18,
        tickfont_size=12,
    ),
    legend=dict(
        x=0.8,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    autosize =True,
    width = 1400,
    height = 600
)

################################################################################################
fig01 = go.Figure()

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[dados['IN_PROF'] == 1]['IN_PROF'].count(),
    domain = {'x': [0, 0.3], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Número de Escolas Técnicas - 2022</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 

fig01.add_trace(go.Indicator(
    mode = "number",
    value = dados.loc[(dados['IN_PROF']==1) & (dados['IN_LABORATORIO_INFORMATICA']== 1)]['IN_PROF'].count(),
    domain = {'x': [0, 0.3], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'><br>Possuem Laboratório de Informática - 2022</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {"font":{"size":68}},
    )) 
fig01.add_trace(go.Indicator(
    mode = "delta",
    value = dados.loc[dados['IN_PROF'] == 1]['IN_PROF'].count(),
    domain = {'x': [0.5, 1], 'y': [0.5, 1]},
    title = {"text": "<span style='font-size:1em'>Aumento Percentual das Escolas de 2007 a 2022</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2007 a 2022 - INEP</span>"},
    delta = {
        'reference': dados_16_anos.loc[(dados_16_anos['NU_ANO_CENSO'] == 2007) & (dados_16_anos['IN_PROF'] == 1)]['IN_PROF'].count(), 
        'relative': True, 
        'valueformat': '.0%',
        'font':{
            'size':64
        }
        },
    number = {"font":{"size":68}}
    )) 
fig01.add_trace(go.Indicator(
    mode = "number",
    value = (dados.loc[(dados['IN_PROF']==1) & (dados['IN_LABORATORIO_INFORMATICA']== 1)]['IN_PROF'].count())/(dados.loc[dados['IN_PROF'] ==1]['IN_PROF'].count())*100,
    domain = {'x': [0.5, 1], 'y': [0, 0.5]},
    title = {"text": "<span style='font-size:1em'>Percentual <span style='font-size:1em;color:red'>COM</span> Laboratórios de Informática - 2022</span><br>"
            "<span style='font-size:0.5em;color:gray'>Fonte: Microdados - Cernso 2022 - INEP</span>"},
    number = {
        "font":{
            "size":68,
            'color':'red'
            }, 
        'suffix':'%',
        'valueformat':'.2f'
        
    },
    
    ))


fig01.update_layout(paper_bgcolor = "lightblue")
###############################################################################################################


layout = html.Div(
    children=[
        html.Div(dcc.Graph(figure=fig, responsive=True)),
        html.Br(),
        html.Div(dcc.Graph(figure=fig01, responsive=True))
        # html.H3('Tipo de conectividade encontrada nas escolas'),
        # dash_table.DataTable(
        #     id='table',
        #     data=df_escolas_profissionalizantes_16_anos.to_dict('records'),
        #     columns=[{'name': i, 'id':i} for i in df_escolas_profissionalizantes_16_anos.columns],
        #     page_action='none',
        #     style_table={'height': '300px', 'overflowY': 'auto', },
        #     style_cell={'textAlign': 'center'},
        #     style_as_list_view=True,
        #     style_header={
        #         'background':'rgb(220, 220, 220)',
        #         'fontWeight': 'bold'
        #     }
        # ),
    ]
)