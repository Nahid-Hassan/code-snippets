import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1('Simple Dash Application!'),
    html.Div('Dash - Data Product Development Framework.'),

    dcc.Graph(
        id = 'simplechar',
        figure = {
            'data' : [
                {'x' : [1,2,3], 'y' : [5,2,3], 'type' : 'bar', 'name': 'Male'},
                {'x' : [1,2,3], 'y' : [10,6,5], 'type' : 'bar', 'name': 'Female'}
            ],
            'layout' : {
                'title' : 'Simple Bar Chart' 
            }
        }
    )    
])

app.run_server(debug=True, port=4000)