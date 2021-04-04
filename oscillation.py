import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


colors = {
    'background': '#110011',
    'text': '#7FDBFF'
}
kset = [i for i in range(10)]




#======== app =====================

app.layout = html.Div(style={'backgroundColor': colors['background']},
    children=[html.H1(
        children='Wave and Oscillation',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    #------fig -1 title setting-----------

    html.Div(children='''
        Two waves
    ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    #------fig 1 visualization -------

    dcc.Graph(id='example-1'),
    dcc.Slider(
        id='k-slider',
        min=min(kset),
        max=max(kset),
        value=2,
        marks={str(i): str(i) for i in kset},
        step=None
    )
])



@app.callback(
    Output('example-1', 'figure'),
    Input('k-slider', 'value'))
def update_figure(selected_k):
    
    x = np.arange(0,selected_k*np.pi,0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = y1+y2

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x,y=y1))
    fig.add_trace(go.Scatter(x=x,y=y2))

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    return fig






#====== Run ===========

if __name__ == '__main__':
    app.run_server( host = '127.0.0.1')






