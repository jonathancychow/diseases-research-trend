import dash
from app.view.layout import main_layout
from app.view.diseases import diseases
from app.view.time import time
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
app.title = 'Diseases'
server = app.server
app.layout = main_layout()

@app.callback(
    [
        Output('entries-graph', 'figure'),
        Output('time-taken-graph', 'figure')
    ],
    [
        Input('submit-button', 'n_clicks_timestamp'),
    ],
    [
        State('year-min', 'value'),
        State('year-max', 'value'),
        State('diseases-type', 'value'),
        State('diseases-area', 'value')
     ])
def plot_entries(timestamp, year_min, year_max, diseases_type, diseases_area):
    fig, time_taken = diseases(year_min, year_max, diseases_type, diseases_area)
    return fig, time(time_taken)


if __name__ == '__main__':
    app.run_server(debug=True)