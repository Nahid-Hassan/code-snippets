import dash
import dash_core_components as dcc
import dash_html_components as html


colors = {
    'plot_bgcolor': '#DDDBE6',
    'paper_bgcolor': '#84838a',
    'text': '#2c2b2e'
}

app = dash.Dash()

app.layout = html.Div([
    html.H1(children='Dash Apps',
            style={
                'textAlign': 'center',
                'color': colors['text'],
            }
            ),
    html.Div(children='Dash - A data driven product.',
             style={
                 'textAlign': 'center'
             }
             ),

    dcc.Graph(
        id='simpleChart',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 5, 6],
                    'type': 'bar', 'name': 'male'},
                {'x': [1, 2, 3], 'y': [10, 50, 39],
                    'type': 'bar', 'name': 'Female'}
            ],
            'layout': {
                'plot_bgcolor': colors['plot_bgcolor'],
                'paper_bgcolor': colors['paper_bgcolor'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Simple Bar Chart with style text'
            }
        }
    )

])

app.run_server(debug=True, port=3000)