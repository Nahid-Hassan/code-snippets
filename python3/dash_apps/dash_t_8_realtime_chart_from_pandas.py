import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('./gapminder_tidy.csv')

app.layout = html.Div([
    dcc.Graph(
        id='scatter_plot',
        figure={
            'data': [
                go.Scatter(
                    x=df.Year,
                    y=df.gdp,
                    mode='markers'
                )
            ],
            'layout': go.Layout(
                title='Scatterplot of Random 60 points',
                xaxis={
                    'title': 'Country'
                },
                yaxis={
                    'title': 'Populations'
                }
            )
        }
    )
])


app.run_server()