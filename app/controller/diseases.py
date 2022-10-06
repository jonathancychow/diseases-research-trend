
import ast
import requests
import urllib.parse
import xml.etree.ElementTree as ET
from enum import Enum
# from database import EntrezDatabases
from app.controller.database import EntrezDatabases
from xml.etree.ElementTree import ParseError

class EUtilityField(Enum):
    TERM = 'term'

class EQueryField(Enum):
    COUNT = 'Count'
    RESULT = 'eGQueryResult'
    ITEM = 'ResultItem'
    ERROR = 'Error'

class Diseases(EntrezDatabases):
    
    # self._data
    def __init__(self) -> None:
        super().__init__()
        self._db_list = self.get_db_list()
        self._parser = ET.XMLParser(encoding="utf-8")

    def payload_string(self, payload)->str:
        return urllib.parse.urlencode(payload, safe=':+')
    
    def get_entries_by_year(self, year, diseases, date_field='dp')-> int:

        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/egquery.fcgi'
        
        payload = {
            EUtilityField.TERM.value: f"{diseases}+AND+{year}[{date_field}]"
        }

        r = requests.get(
                baseURL, 
                params = self.payload_string(payload)
            )

        try:
            xml_root = ET.fromstring(r.text, parser=self._parser)
        except ParseError:
            xml_root = ET.fromstring(r.text)

        entries = [int(result.find(EQueryField.COUNT.value).text) for result in xml_root.find(EQueryField.RESULT.value).findall(EQueryField.ITEM.value) \
            if result.find(EQueryField.COUNT.value).text != EQueryField.ERROR.value]

        return sum(entries)

    def get_data(self, year, diseases)-> int:
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

        # db_list:list = self.get_db_list()
        entry_number =[]
        for db in self._db_list:
            # for month in [f"{year}/01/01:{year}/06/30",f"{year}/07/01:{year}/12/31",]:
                payload = {
                    'db': db, 
                    'term': f'{diseases}+AND+{year}[dp]',
                    'datetype': 'pdat',
                    'retmode': 'json',
                    'retmax': 1
                }

                r = requests.get(
                    baseURL, 
                    params = self.payload_string(payload)
                    )
                data = r.json()
                # numberID = len
                # entry_number.append(len((data['esearchresult']['idlist'])))
                entry_number.append(int(data['esearchresult']['count']))

        return sum(entry_number)

if __name__ == '__main__':
    year = 2019
    # diseases = 'obstetrics'
    diseases = 'cancer'

    import datetime 
    now = datetime.datetime.now()

    d = Diseases()
    # for year in [2016, 2017,2018,2019]:
    for year in range(1960, 2021, 1):
        # print(d.get_data(year, diseases))
        print(d.get_entries_by_year(year, diseases))
    
    finish_time = datetime.datetime.now() - now
    print(f"Took {finish_time.seconds} seconds")