import dash
from app.view.layout import main_layout
from app.view.diseases import diseases
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(external_stylesheets=external_stylesheets)
app.title = 'Diseases'
server = app.server
app.layout = main_layout()

@app.callback(
    [
        Output('entries-graph', 'figure')
    ],
    [
        Input('submit-button', 'n_clicks_timestamp'),
    ],
    [
        State('year-min', 'value'),
        State('year-max', 'value'),
        State('diseases-type', 'value')
     ])
def plot_entries(timestamp, year_min, year_max, diseases_type):

    print(f"min: {year_min}, max:{year_max}, dis:{diseases_type}")
    print(type(diseases_type))
    return diseases(year_min, year_max, diseases_type)


if __name__ == '__main__':
    app.run_server(debug=True)