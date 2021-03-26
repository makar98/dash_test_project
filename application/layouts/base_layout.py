import dash_core_components as dcc
import dash_html_components as html
from application import app

app.layout= html.Div([
            html.Div(id='page-content', className='content')
            ,  dcc.Location(id='url', refresh=False)
        ])