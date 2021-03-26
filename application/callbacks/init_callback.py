import dash

from application.layouts.user.login import login
from application.layouts.user.create import create
from application.layouts.user.sucsses import success
from application.layouts.user.fail import failed
from application.layouts.user.logout import logout

from flask_login import login_user, logout_user, current_user

from application.layouts.base_layout import app
from application.layouts.data_layout import data
from .user import insert_users, successful, update_output
from .data import generate_well, update_1st_scatter, update_2nd_scatter

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return create
    elif pathname == '/login':
        return login
    elif pathname == '/success':
        if current_user.is_authenticated:
            return success
        else:
            return failed
    elif pathname =='/data':
        if current_user.is_authenticated:
            return data
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logout_user()
            return logout
        else:
            return logout
    else:
        return '404'