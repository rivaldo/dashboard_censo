from dash import dcc, html, Input, Output, callback, register_page
import dash_mantine_components as dmc
import plotly.express as px
import pandas as pd

register_page(__name__, icon="fa:bar-chart")

dados_conectividade = pd.read_csv('./assets/data/censo_estadual_2007_a_2022.csv', encoding='latin-1', delimiter=',', low_memory=False)
dados_conectividade.drop(columns='Unnamed: 0', inplace=True)

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    [
        dmc.Select(
            id="dropdown",
            data=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
        ),
        dcc.Graph(id="bar-chart"),
    ]
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig
