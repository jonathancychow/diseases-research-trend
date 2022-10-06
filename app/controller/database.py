import requests
from app.controller.ncbi import NCBI
from app.controller.enum import EInfoField

class EntrezDatabases(NCBI):

    def get_db_list(self)-> list:
        baseURL = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'

        payload = {
            EInfoField.RETMODE.value: 'json',
        }

        r = requests.get(
            baseURL, 
            params = payload
            )

        data = self.get_response_json(r)

        return data[EInfoField.RESULT.value][EInfoField.DB_LIST.value] \
            if EInfoField.RESULT.value in data and EInfoField.DB_LIST.value in data[EInfoField.RESULT.value] else []
