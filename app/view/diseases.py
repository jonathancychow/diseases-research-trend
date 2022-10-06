import datetime 
import plotly.graph_objects as go
from app.controller.diseases import Diseases
from app.model.entry import Entry

def diseases(year_min, year_max, diseases, area):
    fig = go.Figure()
    d = Diseases()
    entry = Entry()
    
    start_time = datetime.datetime.now()

    # x = list(range(year_min, year_max + 1, 1))
    entry._year = list(range(year_min, year_max + 1, 1))
    # y = []
    # for year in x:
    for year in entry._year:
        # y.append(d.get_data(year, diseases))
        # y.append(d.get_entries_by_year(year, diseases))
        entry._entry.append(d.get_entries_by_year(year, diseases, area))

    fig.add_trace(
        go.Scatter(
            x = entry._year, 
            y = entry._entry,
            mode = 'lines',
            name = 'Diseases'
            )
        )
    
    time_taken = datetime.datetime.now() - start_time  

    return fig, time_taken.seconds
