#created by: Wilko
#Project team: TechMasters

import urllib.request


class HTTPClient:
    'The HTTPClient sends and receives data over HTTP'

    def __init__(self):
        self.values = None
        self.headers = {
            'Content-Type': 'application/json',
            'JsonStub-User-Key': 'e2ace556-284c-4b21-9dc5-9900cf4d7236',
            'JsonStub-Project-Key': '7b32ef13-8be8-4e6d-8924-fcc33efb476b'
        }



    def get_data_with_http_request(self, url):
        print("[SERVICES][HTTPCLIENT] sendHTTPRequest")
        request = urllib.request.Request(url,self.values, self.headers)
        response = urllib.request.urlopen(request)
        data = response.read().decode('utf-8')
        print(data)

        return data

