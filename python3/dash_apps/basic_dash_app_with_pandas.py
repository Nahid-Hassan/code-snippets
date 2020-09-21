import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash_table import DataTable

import pandas as pd
df = pd.read_csv('./gapminder_tidy.csv')

app = dash.Dash()

app.layout = html.Div([
    html.H1('Hello SciPy'),

    dcc.Graph(
        id = 'graph',
        figure = {
            'data' : [
                go.Scatter(
                    x = df.Year,
                    y = df.gdp,
                    text = 'Year',
                    type = 'scatter',
                    mode = 'markers'
                )
            ]
        }
    )
    # DataTable(df)
])

if __name__ == "__main__":
    app.run_server(debug=False)