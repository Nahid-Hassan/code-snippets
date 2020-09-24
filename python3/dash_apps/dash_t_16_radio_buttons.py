import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
    html.H1(children='Choose a country',
            style={
                'textAlign': 'center'
            }),
    dcc.Dropdown(
        id='first-dropdown',
        options=[
            {'label': 'Bangladesh', 'value': 'BD'},
            {'label': 'Pakistan', 'value': 'PAK'},
            {'label': 'Turosko', 'value': 'Turky'},
            {'label': 'South Africa', 'value': 'SA', 'disabled': True},
        ],
    ),

    html.Br(),
    html.Br(),

    html.Label('This is Radio Items'),
    html.Br(),
    dcc.RadioItems(
        options=[
            {'label': 'Bangladesh', 'value': 'BD'},
            {'label': 'Pakistan', 'value': 'PAK'},
            {'label': 'Turosko', 'value': 'Turky'},
            {'label': 'South Africa', 'value': 'SA', 'disabled': True},
        ],
        value='BD'
    )
])

app.run_server(debug=True, port=8000)
