import urllib.parse

class NCBI:
    def get_response_json(self, r) -> dict:
        return r.json()

    def get_response_text(self, r) -> str:
        return r.text
    
    def payload_string(self, payload)-> str:
        return urllib.parse.urlencode(payload, safe=':+')
   