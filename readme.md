# Diseases Research Trend

The app is hosted on [Heroku](https://diseases-trend.herokuapp.com/).

At the app, configure the year range, area and the type of diseases, then click the `SUBMIT` button. 

As Heroku's router limits the reqest timeout to be 30 seconds, some of the request would not be possible on the hosted app.  
If you use the following setting, it should avoid the timeout 
- 1980 - 2020
- UK
- Asthma

The router timeout issue is still an outstanding issue I'm trying to resolve but if you run the app locally, the following configuration should take around 45 seconds. 
- 1960 - 2020
- UK
- Cancer

# Getting started
## Set up Environment

`Conda` is used to create a standalone python environment, if conda is not your prefered choice that is no problem at all. Just make sure you are using Python 3.7.13 to minimise chances of running into dependency problem. 

    conda create --name trend python=3.7
    conda activate trend
    pip install -r requirements.txt

## Starting the server
    python main.py

## Testing
### Run Test
    coverage run -m pytest
### Coverage report
    coverage report -m  

        Name                         Stmts   Miss  Cover   Missing
    ----------------------------------------------------------
    app/controller/database.py      10      0   100%
    app/controller/diseases.py      34     11    68%   19-20, 46-66
    app/controller/enum.py          18      0   100%
    app/controller/ncbi.py           8      0   100%
    app/model/entry.py               4      0   100%
    test_main.py                    49      0   100%
    ----------------------------------------------------------
    TOTAL                          123     11    91%
