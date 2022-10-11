import datetime 
import plotly.graph_objects as go
from app.controller.diseases import Diseases
from app.model.entry import Entry

def diseases(year_min:int, year_max:int, diseases:str, area:str):
    print(f"min: {year_min}, max:{year_max}, diseases:{diseases}, area:{area}")

    fig = go.Figure()
    d = Diseases()
    entry = Entry()
    
    start_time = datetime.datetime.now()
    entry.year = list(range(year_min, year_max + 1, 1))
   
    for year in entry.year:
        entry.entry.append(d.get_entries_by_year(year, diseases, area))

    fig.add_trace(
        go.Scatter(
            x = entry.year, 
            y = entry._entry,
            mode = 'lines',
            name = 'Diseases'
            )
        )
    
    time_taken = datetime.datetime.now() - start_time  

    return fig, time_taken.seconds
