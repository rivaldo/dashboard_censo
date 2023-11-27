from dash import dcc, register_page, html
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

df_censo = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', encoding='latin-1', delimiter=',', low_memory=False)
df_censo.drop(columns='Unnamed: 0', inplace=True)

numero = df_censo.groupby('NU_ANO_CENSO')[['NO_ENTIDADE']].count()


cores = []
for ano in numero.index:
    if ano == 2022:
        cores.append('green')
    else:
        cores.append('silver')
        
fig, ax = plt.subplots(figsize=(12,5))
ax.barh(numero.index, numero['NO_ENTIDADE'], color=cores)

for i, v in enumerate(numero['NO_ENTIDADE']):
    ax.text(v + 20,i,  str(v), color='black', fontsize=10, ha='left', va='center')

ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0)
fig.show()


register_page(__name__, path="/", icon="fa-solid:home")



layout = dmc.Container(
    [
        dmc.Title("Dashboard Censo Escolar"),
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
        )
        , html.Div(
            dcc.Graph(figure=fig)
        )
    ]
)
