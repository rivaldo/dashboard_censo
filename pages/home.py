from dash import dcc, register_page, html
import dash_mantine_components as dmc
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df_censo = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', encoding='latin-1', delimiter=',', low_memory=False)
df_censo.drop(columns='Unnamed: 0', inplace=True)

reducao_rede_estadual = df_censo.groupby('NU_ANO_CENSO')[['NO_ENTIDADE']].count()
numero_estudantes = df_censo.groupby('NU_ANO_CENSO')[[ 'QT_MAT_BAS_MASC', 'QT_MAT_BAS_FEM', 'QT_MAT_BAS']].sum()

numero_matriculas_16_anos = df_censo.groupby('NU_ANO_CENSO')[['QT_MAT_BAS', 'QT_MAT_FUND', 'QT_MAT_MED', 'QT_MAT_PROF']].sum()
numero_matriculas_16_anos['NU_ANO_CENSO'] = df_censo['NU_ANO_CENSO'].unique()
numero_matriculas_16_anos.reset_index(drop=True, inplace=True)
numero_matriculas_16_anos['NU_ANO_CENSO'] = pd.to_datetime(numero_matriculas_16_anos['NU_ANO_CENSO'], format='%Y').dt.date
numero_matriculas_16_anos


years = [ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
########GRAFICO REDUÇÃO DE ESCOLAS##################
fig02 = go.Figure()
fig02.add_trace(go.Bar(x=years,
                y=reducao_rede_estadual['NO_ENTIDADE'],
                name='Número de escolas',
                marker_color='rgb(55, 83, 109)', 
                text=reducao_rede_estadual['NO_ENTIDADE']
                ))
fig02.update_xaxes(dtick=[ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
fig02.update_layout(
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

########################################################################

title = 'Comportamento das Matrículas de 2007 a 2022'
labels = ['Ens. Fund.', 'Ens. Médio', 'Ed. Prof.', 'Ed. Básica']
colors = ['rgb(255,0,0)', 'rgb(153,255,204)', 'rgb(0, 153, 0)', 'rgb(255,0,0)']

mode_size = [8, 8, 12, 8]
line_size = [2, 2, 4, 2]

x_data = np.vstack((np.arange(2007, 2023),)*4)

y_data = np.array([
    numero_matriculas_16_anos['QT_MAT_FUND'],
    numero_matriculas_16_anos['QT_MAT_MED'],
    numero_matriculas_16_anos['QT_MAT_PROF'],
    numero_matriculas_16_anos['QT_MAT_BAS'],

])

fig = go.Figure()

for i in range(4):
    fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
        name=labels[i],
        line=dict(color=colors[i], width=line_size[i]),
        connectgaps=True,
    ))

    # endpoints
    fig.add_trace(go.Scatter(
        x=[x_data[i][0], x_data[i][-1]],
        y=[y_data[i][0], y_data[i][-1]],
        mode='markers',
        marker=dict(color=colors[i], size=mode_size[i])
    ))

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

annotations = []

# Adding labels
for y_trace, label, color in zip(y_data, labels, colors):
    annotations.extend(
        (
            dict(
                xref='paper',
                x=0.05,
                y=y_trace[0],
                xanchor='right',
                yanchor='middle',
                text=label + f' {int(y_trace[0])}\n',
                font=dict(family='Arial', size=13),
                showarrow=False,
            ),
            dict(
                xref='paper',
                x=0.95,
                y=y_trace[11],
                xanchor='left',
                yanchor='middle',
                text=f'{int(y_trace[-1])}',
                font=dict(family='Arial', size=13),
                showarrow=False,
            ),
        )
    )
annotations.extend(
    (
        dict(
            xref='paper',
            yref='paper',
            x=0.0,
            y=1.05,
            xanchor='left',
            yanchor='bottom',
            text=title,
            font=dict(family='Arial', size=30, color='rgb(37,37,37)'),
            showarrow=False,
        ),
        dict(
            xref='paper',
            yref='paper',
            x=0.5,
            y=-0.1,
            xanchor='center',
            yanchor='top',
            text='Microdados Censo 2007 a 2022 - ' + 'INEP',
            font=dict(family='Arial', size=12, color='rgb(150,150,150)'),
            showarrow=False,
        ),
    )
)
fig.update_layout(
    annotations=annotations,           
    autosize=True,
    #width=1000,
    #height=600,
)

########################################################################



register_page(__name__, path="/", icon="fa-solid:home")



layout = html.Div(children=[
    html.Br(),
    dcc.Graph(figure=fig02, responsive=True),
    html.Br(),
    html.Br(),
    dcc.Graph(figure=fig, responsive=True),
    html.Br(),
    #dcc.Graph(figure=numero_matriculas, responsive=True),

]

)
