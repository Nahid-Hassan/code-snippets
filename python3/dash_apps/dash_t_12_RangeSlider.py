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

    html.Label('This is a slider'),
    dcc.Slider(
        min = 1, # slider min_value
        max = 10, # slider max_value
        value = 5, # slider position
        step=.5,
        marks = {i : str(i) for i in range(10)} 
    ),

    dcc.RangeSlider(
        min = 1,
        max = 10,
        step = .5,
        value = [3,7],
        marks={i:str(i) for i in range(10)}
    )

])

app.run_server(debug=True, port=8000)
