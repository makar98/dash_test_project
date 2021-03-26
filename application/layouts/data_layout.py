import dash_core_components as dcc
import dash_html_components as html


data = html.Div(
    [html.Div(
        [
        dcc.Input(id='wellname-input', type='text', value='Wellname'),
        html.Button('Generate well',
                    id='generate-well',
                    n_clicks=0)
        ]),
        dcc.Dropdown(id='select-well'),
        html.Div(id='scatter-1-output-container'),
        html.Div(id='scatter-2-output-container'),
    ],
    style={
            'textAlign': 'center',
            'margin': '200px'
        })





