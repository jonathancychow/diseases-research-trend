import dash_html_components as html
import dash_core_components as dcc
from .dash_colours import dash_colors

def main_layout():
    main_layout = html.Div(
        children=[
            html.Div(
                html.H1(children='Diseases Research Trend',
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
                        html.H6(children='Diseases Type',
                        style={
                            'textAlign': 'center',
                            'color': dash_colors['black'],
                        },
                        ),
                        dcc.Dropdown(
                            id='diseases-type',
                            options=[{'label': i, 'value': i}
                                    for i in ['Obstetrics','Asthma','Diabetes','Cancer']],
                            value='Obstetrics',
                            style={
                                'fontSize': 15,
                                'width': '50%',
                                'display': 'inline-block',
                                'verticalAlign': "middle",
                                        },
                                    ),
                        html.H6(children='Area',
                        style={
                            'textAlign': 'center',
                            'color': dash_colors['black'],
                        },
                        ),
                        dcc.Dropdown(
                            id='diseases-area',
                            options=[{'label': i, 'value': i}
                                    for i in ['UK','USA','France','China']],
                            value='UK',
                            style={
                                'fontSize': 15,
                                'width': '50%',
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