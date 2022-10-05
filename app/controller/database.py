import requests

class EntrezDatabases:

    
    def get_db_list(self)-> list:
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'

        payload = {
            'retmode': 'json',
        }

        r = requests.get(
            baseURL, 
            params = payload
            )

        data = r.json()
        return data['einforesult']['dblist'] 

if __name__ == '__main__':
    year = 2019
    # diseases = 'obstetrics'
    diseases = 'cancer'

    d = EntrezDatabases()
    # for year in [2017,2018,2019]:
    print(d.get_db_list())