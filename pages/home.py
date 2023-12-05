from dash import dcc, register_page, html
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df_censo = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', encoding='latin-1', delimiter=',', low_memory=False)
df_censo.drop(columns='Unnamed: 0', inplace=True)

reducao_rede_estadual = df_censo.groupby('NU_ANO_CENSO')[['NO_ENTIDADE']].count()
numero_estudantes = df_censo.groupby('NU_ANO_CENSO')[[ 'QT_MAT_BAS_MASC', 'QT_MAT_BAS_FEM', 'QT_MAT_BAS']].sum()


years = [ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
########GRAFICO REDUÇÃO DE ESCOLAS##################
fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=reducao_rede_estadual['NO_ENTIDADE'],
                name='Número de escolas',
                marker_color='rgb(55, 83, 109)', 
                text=reducao_rede_estadual['NO_ENTIDADE']
                ))
fig.update_xaxes(dtick=[ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
fig.update_layout(
    title='Número de Escolas da Rede Estadual de Educação do Período 2007 a 2022',
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

########GRÁFICO NUMERO DE MATRICULAS TOTAIS, FEMININAS E MASCULINAS##########
numero_matriculas = go.Figure()
""" numero_matriculas.add_trace(go.Bar(x=years,
                y=numero_estudantes['QT_MAT_BAS_MASC'],
                name='Número de matrículas masculinas',
                marker_color='rgb(0,0,255)', 
                text=numero_estudantes['QT_MAT_BAS_MASC']
                ))
numero_matriculas.add_trace(go.Bar(x=years,
                y=numero_estudantes['QT_MAT_BAS_FEM'],
                name='Número de matrículas femininas',
                marker_color='rgb(255,0,0)', 
                text=numero_estudantes['QT_MAT_BAS_FEM']
                )) """
numero_matriculas.add_trace(go.Bar(x=years,
                y=numero_estudantes['QT_MAT_BAS'],
                name='Número de matrícula total',
                marker_color='rgb(55, 83, 109)', 
                text=numero_estudantes['QT_MAT_BAS']
                ))
numero_matriculas.update_xaxes(dtick=[ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
numero_matriculas.update_layout(
    title='Número de Matriculas da Educação Básica do Período 2007 a 2022',
    title_font_size=22,
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Número de Matriculas',
        titlefont_size=14,
        tickfont_size=12,
    ),
    legend=dict(
        x=0.7,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.09, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1, # gap between bars of the same location coordinate.
    autosize =True,
    width = 1400,
    height = 600
)



register_page(__name__, path="/", icon="fa-solid:home")



layout = html.Div(children=[
    html.Br(),
    dcc.Graph(figure=fig, responsive=True),
    html.Br(),
    dcc.Graph(figure=numero_matriculas, responsive=True),

]
            
)
