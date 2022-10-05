# from requests import get
import requests
import urllib.parse

class Diseases:
    baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

    def payload_string(self, payload)->str:
        return urllib.parse.urlencode(payload, safe=':+')
    
    def get_data(self, year, diseases):
        payload = {
            'db': 'pubmed', 
            'term': f'{diseases}+AND+{year}[dp]',
            'datetype': 'pdat',
            'retmode': 'json',
            'retmax': 100000
        }

        r = requests.get(
            self.baseURL, 
            params = self.payload_string(payload)
            )
        data = r.json()
        numberID = len(data['esearchresult']['idlist'])
        return numberID 

if __name__ == '__main__':
    year = 2019
    diseases = 'obstetrics'
    d = Diseases()
    for year in [2017,2018,2019]:
        print(d.get_data(year, diseases))