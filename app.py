# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import datetime
import plotly.express as px
import requests


l = []
url = 'https://digital-summer.sk.kz/case_files/1585048700_IxotsoGPwgKgSWkVjzkmt4e0Wh907PJh.json'
data = (requests.get(url=url)).json()
for d in data:
    l.append(int(datetime.datetime.fromtimestamp(
    d["timestamp"]
).strftime('%H')))

hours = {}  
for i in range(8,19):
    s=str(i)+":00 - " +str(i+2) + ":00"
    hours[s]=l.count(i)+l.count(i+1)

fig = px.pie(values=list(hours.values()), names=list(hours.keys()))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Digital Summer Dashboard',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H2(children='Bar Chart', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='bar',
        figure={
            'data': [
                {'x': list(hours.keys()), 'y': list(hours.values()), 'type': 'bar', 'title': 'Bar Chart'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    html.H2(children='Pie Chart', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(figure=fig),

    html.H3(children='Created by Akzhol Baktiyar', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
])

if __name__ == '__main__':
    app.run_server(debug=True)