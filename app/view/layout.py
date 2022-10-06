import dash_html_components as html
import dash_core_components as dcc
from .dash_colours import dash_colors

def main_layout():
    main_layout = html.Div(
        children=[
            html.Div(
                html.H1(children='Diseases Research Articles Trend',
                        style={
                            'textAlign': 'center',
                            'color': dash_colors['black'],
                        },
                        )
            ),
            html.Div([
                dcc.Graph(id='entries-graph'),
                dcc.Input(id='year-min', type='number', value=2016, min=1900, max=2022, step=1),
                dcc.Input(id='year-max', type='number', value=2018, min=1900, max=2022, step=1),
            ],
                style={
                    'textAlign': 'center',
                    'color': dash_colors['text'],
                    'width': '100%',
                    'float': 'center',
                    'display': 'inline-block'}

            ),
            html.Div([
                dcc.Dropdown(
                    id='diseases-type',
                    options=[{'label': i, 'value': i}
                             for i in ['obstetrics','cancer']],
                    value='obstetrics',
                    style={
                        'fontSize': 15,
                        'width': '100%',
                        'display': 'inline-block',
                        'verticalAlign': "middle",
                                },
                            ),
                        ],
                style={
                    'textAlign': 'center',
                    'color': dash_colors['text'],
                    'width': '100%',
                    'float': 'center',
                    'display': 'inline-block'}
            ),
            html.Button('Submit', id='submit-button', n_clicks=0, style={
                    'textAlign': 'center',
                    'color': dash_colors['black'],
                    'width': '100%',
                    'float': 'center',
                    'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id='time-taken-graph')
                ]),
        ]
    )
    return main_layout