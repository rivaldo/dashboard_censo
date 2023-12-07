import dash
from dash import dcc, html, Output, Input, State
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import matplotlib.pyplot as plt
import dash_bootstrap_components as dbc
import os


header_style = {
    "display": "flex",  # Use Flexbox layout
    "justifyContent": "space-between",  # Align children with space between (left and right)
    "alignItems": "center",  # Center the content vertically (top and bottom)
    #"border-bottom": "solid grey 3px",
    #"border": f"1px solid {dmc.theme.DEFAULT_COLORS['green'][4]}",
    "background-color": "#f7f7fa",
}

container_style = {
    "display": "flex",  # Use Flexbox layout
    "justifyContent": "space-between",  # Align children with space between (left and right)
    "width": "90%",  # Stretch container to 100% of the page width
    "height": "100%",  # Stretch container to 100% of the page width
    #"border": f"1px solid {dmc.theme.DEFAULT_COLORS['blue'][4]}",
}

avatar_style = {
    "margin-left": "auto",  # Display the avatar on the right side of the container
    "height": "95%",
    "padding-top": "1px",
}


app = dash.Dash(
    __name__, 
    use_pages=True, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)


def create_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            [
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    variant="light",
                ),
                dmc.Text(label, size="sm", color="gray"),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )


sidebar = dmc.Navbar(
    fixed=True,
    width={"base": 300},
    position={"top": 100},
    height=300,
    children=[
        dmc.ScrollArea(
            offsetScrollbars=True,
            type="scroll",
            children=[
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon="radix-icons:home",
                            label="Inicio",
                            href="/",
                        ),
                    ],
                ),
                dmc.Divider(
                    label="Capitulo 1", style={"marginBottom": 20, "marginTop": 20}
                ),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter1")
                    ],
                ),
                dmc.Divider(
                    label="Chapter 2", style={"marginBottom": 20, "marginTop": 20}
                ),
                dmc.Stack(
                    children=[
                        create_nav_link(
                            icon=page["icon"], label=page["name"], href=page["path"]
                        )
                        for page in dash.page_registry.values()
                        if page["path"].startswith("/chapter2")
                    ],
                ),
            ],
        )
    ],
)

app.layout = dmc.Container(
    [
        dmc.Header(
            height=80,
            children=[
                dmc.Container(
                    children=[
                        html.H2(children="Dashboard Censo da Educação - Rede Estadual", style={"margin-left": "10px", "padding-top": "-5px"}),
                        html.Img(
                            src='./assets/logo_see.jpeg',
                            alt="Logomarca SEE",
                            style=avatar_style
                        ),
                    ], size="xl", px="xl", style=container_style,
                ),
            ], style=header_style,
        ),
        sidebar,
        dmc.Container(
            dash.page_container,
            size="lg",
            pt=20,
            style={"marginLeft": 300},
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
