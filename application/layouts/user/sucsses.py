import dash_core_components as dcc
import dash_html_components as html


success = html.Div([dcc.Location(id='url_login_success', refresh=True)
            , html.Div([html.H2('Login successful.')
                    , html.Br()
                    , html.P('Select a Dataset')
                    , dcc.Link('Data', href = '/data')
                ])
            , html.Div([html.Br()
                    , html.Button(id='back-button', children='Go back', n_clicks=0)
                ])
        ])