import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc 
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash()

app.layout = html.Div([
    html.H1('Hello Scipy'),

    dcc.Markdown('''
        The first part of a Dash apps in the 'layout' of the app, or what the app looks like.
    '''),

    dcc.Graph(
        id='graph',
        figure = {
            'data' : [
                go.Bar(x=[1,2,3],y = [4,1,2])
            ]
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)