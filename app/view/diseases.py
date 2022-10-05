import plotly.graph_objects as go
from app.controller.diseases import Diseases

def diseases(year_min, year_max, diseases):
    fig = go.Figure()
    d = Diseases()
    x = list(range(year_min, year_max + 1, 1))
    y = []
    for year in x:
        y.append(d.get_data(year, diseases))

    fig.add_trace(
        go.Scatter(
            x = x, 
            y = y,
            mode = 'lines',
            name = 'Diseases'
            )
        )
    return fig          
