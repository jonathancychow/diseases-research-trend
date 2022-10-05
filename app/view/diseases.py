# from src.toolbox.SignalProcessing import moving_average
# from src.fetch.visualise_country import get_country_data
import plotly.graph_objects as go
# from src.fetch.get_population import  get_countries_population_df
from app.controller.get_data import Diseases

# countries_population_df = get_countries_population_df()


def diseases(country, unit):
    fig = go.Figure()
    year = 2019
    diseases = 'obstetrics'
    d = Diseases()
    x = [2017,2018,2019]
    y = []
    for year in [2017,2018,2019]:
        # print(d.get_data(year, diseases))
        y.append(d.get_data(year, diseases))

    fig.add_trace(
        go.Scatter(
            x = x, 
            y = y,
            mode = 'lines',
            name = 'dfsfsfsdf'
            )
        )
    return fig          
    # status = 'confirmed'
    # for thisCountry in country:
    #     date, cumulativeCase, dailyCase = get_country_data(thisCountry, status)
    #     if unit == 'Per 100,000':
    #         global countries_population_df
    #         dailyCase = [100000 * x / countries_population_df[thisCountry] for x in dailyCase]
    #     x = date
    #     y = dailyCase
    #     N = 7
    #     y_mva = moving_average(dailyCase, N)

    #     fig.add_trace(go.Scatter(x=date, y=y_mva,
    #                              mode='lines',
    #                              name=thisCountry)
    #                   )
    # fig.update_layout(template="plotly_white",
    #                   title={
    #                       'text': "Europe - Confirmed Daily Cases",
    #                       'x': 0.5,
    #                       'xanchor': 'center',
    #                       'yanchor': 'top'}
    #                   )
    # return fig
