import dash_html_components as html
import dash_core_components as dcc
from .dash_colours import dash_colors
# from src.frontend.colour.dash_colours import dash_colors

def main_layout():
    main_layout = html.Div(
        children=[
            html.Div(
                html.H1(children='COVID 19 Cases Dashboard',
                        style={
                            'textAlign': 'center',
                            # 'color': dash_colors['black'],
                        },
                        )
            ),
            html.Div([
                dcc.Graph(id='countries-graph'),
                dcc.Dropdown(
                    id='plot-countries-case',
                    multi=True,
                    options=[{'label': i, 'value': i}
                             for i in ['United-Kingdom', 'Spain', 'France', 'Belgium','Germany',
                                       'Italy','Switzerland','Luxembourg',
                                       'Denmark','Sweden','Norway','Poland','Ukraine','Belarus']],
                    value=['United-Kingdom', 'Spain', 'France'],
                    style={
                        'fontSize': 15,
                        'width': '100%',
                        'display': 'inline-block',
                        'verticalAlign': "middle",
                    },
                )
            ],
                style={
                    'textAlign': 'center',
                    'color': dash_colors['text'],
                    'width': '40%',
                    'float': 'center',
                    'display': 'inline-block'}

            ),
        ]
    )
    return main_layout