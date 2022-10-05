# from requests import get
import requests
import urllib.parse
from database import EntrezDatabases
# from app.controller.database import EntrezDatabases

class Diseases(EntrezDatabases):
    
    # self._data
    def __init__(self) -> None:
        super().__init__()
        self._db_list = self.get_db_list()

    def payload_string(self, payload)->str:
        return urllib.parse.urlencode(payload, safe=':+')
    
    def get_data(self, year, diseases)-> int:
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

        # db_list:list = self.get_db_list()
        entry_number =[]
        for db in self._db_list:
            for month in [f"{year}/01/01:{year}/06/30",f"{year}/07/01:{year}/12/31",]:
                payload = {
                    'db': db, 
                    'term': f'{diseases}+AND+{month}[dp]',
                    'datetype': 'pdat',
                    'retmode': 'json',
                    'retmax': 100000
                }

                r = requests.get(
                    baseURL, 
                    params = self.payload_string(payload)
                    )
                data = r.json()
                # numberID = len
                entry_number.append(len((data['esearchresult']['idlist'])))
        
        return sum(entry_number)

if __name__ == '__main__':
    year = 2019
    # diseases = 'obstetrics'
    diseases = 'cancer'

    import datetime 
    now = datetime.datetime.now()

    d = Diseases()
    for year in [2016, 2017,2018,2019]:
        print(d.get_data(year, diseases))
    
    finish_time = datetime.datetime.now() - now
    print(f"Took {finish_time.seconds} seconds")