import dash
import json as json
import numpy as np
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
from datetime import datetime
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

colors = {
    'left-panel': '#020b1a',
    'background': '#132a4f',
    'right-panel':'#020b1a',
    'text': 'white'
}



#============API-data==================
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

history_url = "https://financialmodelingprep.com/api/"+\
      "v3/historical-chart/1min/AAPL?apikey=xxxx"
history_data = get_jsonparsed_data(history_url)
history_df = pd.DataFrame(history_data)
history_df['index'] = [i for i in range(history_df.shape[0])]


profile_url = "https://financialmodelingprep.com/api/"+\
              "v3/profile/AAPL?apikey=xxxx"
profile_data = get_jsonparsed_data(profile_url)
profile_df = pd.DataFrame(profile_data)

#=====figure===================================
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x = np.array(history_df['index']),y=np.array(history_df['open'])))
fig1.add_trace(go.Scatter(x = np.array(history_df['index']),y=np.array(history_df['close'])))
fig1.add_trace(go.Scatter(x = np.array(history_df['index']),y=np.array(history_df['high'])))

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])



#=====figure==================================
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x = np.array(history_df['index']),y=np.array(history_df['volume'])))


fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])

fig3 = go.Figure()
fig3.add_trace(go.Candlestick(
        x=np.array(history_df['index']),
        open=np.array(history_df['open']),
        high=np.array(history_df['high']),
        low=np.array(history_df['low']),
        close=np.array(history_df['close'])
    ))
fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])



#=======app====================================
app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                    html.Div(className='four columns div-user-controls',
                             children=[
                                 html.H2('DASH - STOCK PRICES'),
                                 html.P('Visualising time series with Plotly - Dash.'),
                                 html.P('Pick one or more stocks from the dropdown below.'),
                                 html.P('Symbol: ' + profile_data[0]['symbol']),
                                 html.P('Profile: ' +  profile_data[0]['description']),
                                 html.P('Volume: ' + profile_data[0]['volAvg']),
                                 html.P('Market Cap: ' + profile_data[0]['mktCap'])
                                ]
                             ),
                    html.Div(className='eight columns div-for-charts bg-grey',
                             children=[                 
                             dcc.Graph(figure=fig1),
                             dcc.Graph(figure=fig2),
                             dcc.Graph(figure=fig3)
                             ])
                              ])
        ])



#========run============

if __name__ == '__main__':
  #print(df.head())
  print(profile_data)
  app.run_server(host = '127.0.0.1')
