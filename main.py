import pandas as pd # 0.23.0
import requests     # 2.19.1
import io

url_endpoint = 'https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes'

payload = {
    'Datefrom'   : '25/Aug/2022',
    'Dateto'     : '26/Aug/2022',
    'SeriesCodes': 'XUDLGBD',
    'CSVF'       : 'TN',
    'UsingCodes' : 'Y',
    'VPD'        : 'Y',
    'VFD'        : 'N'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.90 '
                  'Safari/537.36'
}

response = requests.get(url_endpoint, params=payload, headers=headers)

print(response.status_code)
print(response.url)
print(response.text)
