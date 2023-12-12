from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd

register_page(__name__, icon="ph:squares-four-duotone")
##################################LEITURA DO DATASET#########################
dados_16_anos = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', sep=',', low_memory=False, encoding='latin-1', index_col='NU_ANO_CENSO')
dados_16_anos.drop(columns='Unnamed: 0', inplace=True)
dados_16_anos.index = pd.to_datetime(dados_16_anos.index, format='%Y')
##############################################################################

numero_matriculas_16_anos_cor_raca = dados_16_anos.groupby(dados_16_anos.index)[['QT_MAT_BAS_ND', 'QT_MAT_BAS_BRANCA', 'QT_MAT_BAS_PRETA', 'QT_MAT_BAS_PARDA', 'QT_MAT_BAS_AMARELA', 'QT_MAT_BAS_INDIGENA']].sum()

numero_matriculas_16_anos_cor_raca.rename(
    columns={
        'QT_MAT_BAS_ND':'COR/RAÇA NÃO DECLARADA', 
        'QT_MAT_BAS_BRANCA':'COR/RAÇA BRANCA', 
        'QT_MAT_BAS_PRETA':'COR/RAÇA PRETA', 
        'QT_MAT_BAS_PARDA':'COR/RAÇA PARDA', 
        'QT_MAT_BAS_AMARELA':'COR/RAÇA AMARELA', 
        'QT_MAT_BAS_INDIGENA':'COR/RAÇA INDIGENA'
    },
    inplace=True
)
numero_matriculas_16_anos_cor_raca.rename_axis('Ano do Censo', inplace=True)


layout = html.Div([
    html.H4('Número de matriculas por Raça e Cor'),
    dcc.Graph(id="time-series-chart"),
    html.P("Selecione Cor/Raça: "),
    dcc.Dropdown(
        id="ticker",
        options=numero_matriculas_16_anos_cor_raca.columns,
        value=numero_matriculas_16_anos_cor_raca.columns[0],
        clearable=False,
    ),
])


@callback(
    Output("time-series-chart", "figure"), 
    Input("ticker", "value"))
def display_time_series(ticker):
    numero_matriculas_16_anos_cor_raca # replace with your own data source
    return px.line(
        numero_matriculas_16_anos_cor_raca,
        x=numero_matriculas_16_anos_cor_raca.index,
        y=ticker,
        markers=True,
    )
