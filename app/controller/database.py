import requests
from app.controller.ncbi import NCBI

class EntrezDatabases(NCBI):

    def get_db_list(self)-> list:
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'

        payload = {
            'retmode': 'json',
        }

        r = requests.get(
            baseURL, 
            params = payload
            )

        # data = r.json()
        data = self.get_response_json(r)
        
        return data['einforesult']['dblist'] if 'einforesult' in data and 'dblist' in data['einforesult'] else []

if __name__ == '__main__':
    year = 2019
    # diseases = 'obstetrics'
    diseases = 'cancer'

    d = EntrezDatabases()
    # for year in [2017,2018,2019]:
    print(d.get_db_list())