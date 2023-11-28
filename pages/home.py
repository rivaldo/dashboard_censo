from dash import dcc, register_page, html
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df_censo = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', encoding='latin-1', delimiter=',', low_memory=False)
df_censo.drop(columns='Unnamed: 0', inplace=True)

reducao_rede_estadual = df_censo.groupby('NU_ANO_CENSO')[['NO_ENTIDADE']].count()


years = [ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=reducao_rede_estadual['NO_ENTIDADE'],
                name='n',
                marker_color='rgb(55, 83, 109)', 
                text=reducao_rede_estadual['NO_ENTIDADE']
                ))
fig.update_xaxes(dtick=[ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 
        2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
fig.update_layout(
    title='Redução do Número de Escolas da Rede Estadual de Educação de 2007 a 2022',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Número de Escolas',
        titlefont_size=14,
        tickfont_size=12,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()




register_page(__name__, path="/", icon="fa-solid:home")



layout = dmc.Container(
    [
        #dmc.Title("Dashboard Censo Escolar"),
        dcc.Markdown(
            """
            This is a demo of a multi-page app with nested folders in the `pages` folder.  
            
            For example:            
            ```
            - app.py 
            - pages
                - chapter1                  
                   |-- page1.py
                   |-- page2.py
                - chapter2                   
                   |-- page1.py
                   |-- page2.py    
                - home.py        
            ```
                        
            This app also demos how to add arbitrary data to the `page_registry`.  This example adds icons to the `page_registry`
            
            ```
            dash.register_page(__name__, icon="fa:bar-chart")
            
            ```
            
            In `app.py` we loop through `dash.page_registry` to create the links:
            
            ```
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter2")
                    ],
            ``` 
            
            """
        ),
        html.Div(
            dcc.Graph(figure=fig)
        )
        
    ]
)
