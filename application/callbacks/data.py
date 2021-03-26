import dash_core_components as dcc
import dash
import plotly.express as px
import plotly.graph_objs as go
from application import app
from application.data_generation.generate import generate as art_well_data_generation
from flask_login import current_user

from application.models import Well

@app.callback(
    dash.dependencies.Output('select-well', 'options'),
    dash.dependencies.Output('select-well', 'value'),
    dash.dependencies.Input('generate-well', 'n_clicks'),
    dash.dependencies.State('wellname-input', 'value'))
def generate_well(n_clicks, wellname):
    if n_clicks != 0:
        well_id = art_well_data_generation(1, [wellname], user_id=current_user.id)[0].id
        wells = Well.query.filter_by(user_id=current_user.id).all()
        opt = []
        for w in wells:
            sel = {'label': w.name, 'value': w.id}
            opt.append(sel)
        return opt, well_id
    wells = Well.query.filter_by(user_id=current_user.id).all()
    opt = []
    for w in wells:
        sel = {'label': w.name, 'value': w.id}
        opt.append(sel)
    if len(wells) > 0:
        well_id = wells[0].id
    else:
        well_id = ''
    return opt, well_id


@app.callback(
    dash.dependencies.Output('scatter-1-output-container', 'children'),
    [dash.dependencies.Input('select-well', 'value')])
def update_1st_scatter(value):
    well = Well.query.filter_by(id=value).first()
    if well:
        min = [d.min for d in well.data]
        gas = [d.gas for d in well.data]
        oil = [d.oil for d in well.data]
        water = [d.water for d in well.data]
        # import numpy
        # gas_mean = numpy.array(gas).mean()
        # oil_mean = numpy.array(oil).mean()
        # water_mean = numpy.array(water).mean()
        # print(gas_mean, oil_mean, water_mean)

        fig = go.Figure(data=[go.Scatter(x=min, y=gas, name='gas'),
                                go.Scatter(x=min, y=oil, name='oil'),
                                go.Scatter(x=min, y=water, name='water')
                                ]
                          )
        graph = dcc.Graph(figure=fig)
    else:
        graph = ''
    return graph

@app.callback(
    dash.dependencies.Output('scatter-2-output-container', 'children'),
    [dash.dependencies.Input('select-well', 'value')])
def update_2nd_scatter(value):
    well = Well.query.filter_by(id=value).first()
    if well:
        fig_1 = px.scatter(x=[d.water for d in well.data],
                           y=[d.oil for d in well.data],
                           labels={'x': 'Water', 'y': 'Oil'})
        graph = dcc.Graph(figure=fig_1)
    else:
        graph = "You haven't created a well"
    return graph