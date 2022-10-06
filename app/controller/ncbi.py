import requests
import urllib.parse


class NCBI:
    def get_response_json(self, r:requests.models.Response) -> dict:
        return r.json()

    def get_response_text(self, r:requests.models.Response) -> str:
        return r.text
    
    def payload_string(self, payload:dict)-> str:
        return urllib.parse.urlencode(payload, safe=':+')
   