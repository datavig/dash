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
    'left-panel': '#020b1a',
    'background': '#132a4f',
    'right-panel':'#020b1a',
    'text': 'white'
}

kset = [i for i in range(10)]
wset = [i for i in range(10)]




#======== app =====================

app.layout = html.Div(style={'backgroundColor': colors['background']},
                    children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls',
                                  style={'backgroundColor': colors['left-panel']},
                                  children = [
                                        html.H2('Wave and Superposition',
                                            style={'textAlign': 'center','color': colors['text']}),

                                        html.P('''Visualising time series with Plotly - Dash''',
                                            style={'textAlign': 'center','color': colors['text']}),                                       
                                        dcc.Slider(id='k-slider',min=min(kset),
                                                max=max(kset),value=2,marks={str(i): str(i) for i in kset},step=None)                                       
                                    ]),  


                                  html.Div(className='eight columns div-for-charts bg-grey',
                                  style={'backgroundColor': colors['right-panel']},
                                  children = [
                                        html.H2('Wave and Superposition',
                                            style={'textAlign': 'center','color': colors['text']}),
                                        
                                        dcc.Graph(id='example-1'),
                                    ])  
                                  ])
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






