import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

df = pd.read_csv('./gapminder_tidy.csv')
country_name = df.Country
country_name = list(country_name.unique())

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
        ],
        value='BD'
    )
])

app.run_server(debug=True, port=4000)
