import plotly.graph_objects as go
from .dash_colours import dash_colors

def time(time=0):
    return {
        'data': [{'type': 'indicator',
                  'mode': 'number',
                  'value': time,
                  'number': {'valueformat': ',',
                             'font': {'size': 30}},
                  'domain': {'y': [0, 1], 'x': [0, 1]}}],
        'layout': go.Layout(
            title={'text': "Seconds for query to complete"},
            font=dict(color='black'),
            paper_bgcolor='white',
            plot_bgcolor=dash_colors['background'],
            height=200
        )
    }