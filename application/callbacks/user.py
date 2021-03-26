import dash_core_components as dcc
import dash_html_components as html
import dash

from application import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from application.layouts.user.login import login
from application.models import User
from flask_login import login_user, logout_user, current_user

@app.callback(
   [dash.dependencies.Output('container-button-basic', "children")],
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('username', 'value'),
     dash.dependencies.State('password', 'value'),
     dash.dependencies.State('email', 'value')
     ])
def insert_users(n_clicks, un, pw, em):
    hashed_password = generate_password_hash(pw, method='sha256')
    if un is not None and pw is not None and em is not None:
        u = User(username=un, password=hashed_password, email=em)
        db.session.add(u)
        db.session.commit()
        return [login]
    else:
        return [html.Div([html.H2('Already have a user account?'),
                          dcc.Link('Click here to Log In', href='/login')
                          ]
                         )
                ]

@app.callback(
    dash.dependencies.Output('url_login', 'pathname'),
    [dash.dependencies.Input('login-button', 'n_clicks')],
    [dash.dependencies.State('uname-box', 'value'),
     dash.dependencies.State('pwd-box', 'value')
     ])
def successful(n_clicks, username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user)
            return '/data'
        else:
            pass
    else:
        pass

@app.callback(
    dash.dependencies.Output('output-state', 'children'),
    [dash.dependencies.Input('login-button', 'n_clicks')],
    [dash.dependencies.State('uname-box', 'value'),
     dash.dependencies.State('pwd-box', 'value')
     ])
def update_output(n_clicks, username, password):
    if n_clicks > 0:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''