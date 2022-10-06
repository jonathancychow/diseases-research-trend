import plotly.graph_objects as go
from app.controller.diseases import Diseases
from app.model.entry import Entry

def diseases(year_min, year_max, diseases):
    fig = go.Figure()
    d = Diseases()
    entry = Entry()
    # x = list(range(year_min, year_max + 1, 1))
    entry._year = list(range(year_min, year_max + 1, 1))
    # y = []
    # for year in x:
    for year in entry._year:
        # y.append(d.get_data(year, diseases))
        # y.append(d.get_entries_by_year(year, diseases))
        entry._entry.append(d.get_entries_by_year(year, diseases))

    fig.add_trace(
        go.Scatter(
            x = entry._year, 
            y = entry._entry,
            mode = 'lines',
            name = 'Diseases'
            )
        )
    return fig          
