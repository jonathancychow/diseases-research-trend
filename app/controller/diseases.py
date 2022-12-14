
import requests
import xml.etree.ElementTree as ET

from app.controller.enum import EUtilityField, EQueryField, ESearchField
from app.controller.database import EntrezDatabases
from ratelimit import limits, sleep_and_retry
from xml.etree.ElementTree import ParseError

class XmlParsingException(Exception):
    pass
class Diseases(EntrezDatabases):
    
    def __init__(self) -> None:
        super().__init__()
        self._db_list = self.get_db_list()
        self._parser = ET.XMLParser(encoding="utf-8")

    def parse_xml(self, xml_string:str):
        try:
            if '"error":"API rate limit exceeded"' in xml_string:
                raise XmlParsingException("rate limit exceeded")
            xml_root = ET.fromstring(xml_string)
        except ParseError:
            xml_root = ET.fromstring(xml_string, parser=self._parser)
        return xml_root

    @sleep_and_retry
    @limits(calls=1, period=1)
    def make_request(self, payload:str):
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/egquery.fcgi'
        return requests.get(
                baseURL, 
                params = self.payload_string(payload)
            )

    def get_entries_by_year(self, year:int, diseases:str, area:str, date_field='dp')-> int:
        
        payload = {
            EUtilityField.TERM.value: f"{diseases}+AND+{area}+AND+{year}[{date_field}]"
        }

        response = self.make_request(payload)

        response_text:str = self.get_response_text(response)
        xml_root = self.parse_xml(response_text)

        entries = [int(result.find(EQueryField.COUNT.value).text) for result in xml_root.find(EQueryField.RESULT.value).findall(EQueryField.ITEM.value) \
            if result.find(EQueryField.COUNT.value).text != EQueryField.ERROR.value]

        return sum(entries)

    def get_entries_esearch(self, year:int, diseases:str)-> int:

        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi'

        entry_number =[]
        for db in self._db_list:
            for month in [f"{year}/01/01:{year}/06/30",f"{year}/07/01:{year}/12/31",]:
                payload = {
                    ESearchField.DB.value: db, 
                    ESearchField.TERM.value: f'{diseases}+AND+{year}[dp]',
                    ESearchField.DATATYPE.value: 'pdat',
                    ESearchField.RETMODE.value: 'json',
                    ESearchField.RETMAX.value: 1
                }

                r = self.make_request(payload)
                data:dict = r.json()
                entry_number.append(int(data[ESearchField.RESULT.value][ESearchField.COUNT.value]))

        return sum(entry_number)
