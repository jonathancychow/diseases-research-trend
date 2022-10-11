import concurrent.futures
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
   
    # from concurrent.futures import ThreadPoolExecutor
    # pool = ThreadPoolExecutor(workers=6)

    # for year in entry.year:
    #     entry.entry.append(d.get_entries_by_year(year, diseases, area))

   
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_response = {executor.submit(d.get_entries_by_year, year, diseases, area): year for year in entry.year}
        for future in concurrent.futures.as_completed(future_response):
            entry.year.append(future_response[future])
            try:
                entry.entry.append(future.result())
            except Exception as exc:
                print(f'{future_response[future]} generated an exception: {exc}')
            
            # try:
            #     data = future.result()
            # except Exception as exc:
            #     print('%r generated an exception: %s' % (url, exc))
            # else:
            #     print('%r page is %d bytes' % (url, len(data)))

    entry.year, entry.entry = zip(*sorted(zip(entry.year, entry.entry)))

    fig.add_trace(
        go.Scatter(
            x = entry.year, 
            y = entry.entry,
            # x = result_year,
            # y = result,
            mode = 'lines',
            name = 'Diseases'
            )
        )
    
    time_taken = datetime.datetime.now() - start_time  

    return fig, time_taken.seconds
