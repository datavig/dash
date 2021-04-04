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
    'background': '#111111',
    'text': '#7FDBFF'
}

#=======data================

k = 10
x = np.arange(0,k*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1+y2

#========= Figure ============

#--fig 1 ---------------------

fig1 = go.Figure()
fig1.add_trace(
    go.Scatter(x=x,y=y1)
    )
fig1.add_trace(
    go.Scatter(x=x,y=y2)
    )
fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#--fig 1 ---------------------

fig2 = go.Figure()
fig2.add_trace(
    go.Scatter(x=x,y=y1)
    )
fig2.add_trace(
    go.Scatter(x=x,y=y2)
    )

fig2.add_trace(
    go.Scatter(x=x,y=y3)
    )

fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])


#-----fig 3 --------------

fs = 100
ts = np.arange(0,60,1/fs)

fig3 = go.Figure()
for i in range(1,10):
    amp = 100*1/float(i)
    freq = 0.025*i

    '''Y= A sin(wt) | w = 2*pi*f'''
    ys = amp*np.sin(ts*2*np.pi*freq)
    fig3.add_trace(go.Scatter(x=ts,y=ys))

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])
    


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

    dcc.Graph(
        id='example-graph1',
        figure=fig1
    ),

    #------fig -2 title setting-----------

    html.Div(children='''
        Superposition
    ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    #------fig 2 visualization -------


    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),

    #------fig -3 title setting-----------

    html.Div(children='''
        Many Oscillations: Sine curves
    ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

    #------fig 2 visualization -------


    dcc.Graph(
        id='example-graph3',
        figure=fig3
    )

])






#====== Run ===========

if __name__ == '__main__':
    app.run_server( host = '127.0.0.1')






