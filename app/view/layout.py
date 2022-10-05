import dash_html_components as html
import dash_core_components as dcc
from .dash_colours import dash_colors
# from src.frontend.colour.dash_colours import dash_colors

def main_layout():
    main_layout = html.Div(
        children=[
            html.Div(
                html.H1(children='Diseases Research Articles Trend',
                        style={
                            'textAlign': 'center',
                            # 'color': dash_colors['black'],
                        },
                        )
            ),
            html.Div([
                dcc.Graph(id='countries-graph'),
                dcc.Input(id='year-min', type='number', value=2018, min=1900, max=2022, step=1),
                dcc.Input(id='year-max', type='number', value=2020, min=1900, max=2022, step=1),
                # dcc.Dropdown(
                #     id='plot-countries-case',
                #     multi=True,
                #     options=[{'label': i, 'value': i}
                #              for i in ['United-Kingdom', 'Spain', 'France', 'Belgium','Germany',
                #                        'Italy','Switzerland','Luxembourg',
                #                        'Denmark','Sweden','Norway','Poland','Ukraine','Belarus']],
                #     value=['United-Kingdom', 'Spain', 'France'],
                #     style={
                #         'fontSize': 15,
                #         'width': '100%',
                #         'display': 'inline-block',
                #         'verticalAlign': "middle",
                #     },
                # )
            ],
                style={
                    'textAlign': 'center',
                    'color': dash_colors['text'],
                    'width': '100%',
                    'float': 'center',
                    'display': 'inline-block'}

            ),
        ]
    )
    return main_layout