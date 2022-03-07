
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from data_domains import data

# Test how many domains accepts requests

domains_ok = []
domains_ko = []
error_type = {}
for i in range(150):
    url = data[i]
    print(url)
    session = requests.Session()
    retry = Retry(connect=1, backoff_factor=0.5)
    #retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    try: 
        s = session.get(url,verify=False)
    except requests.exceptions.Timeout:
        print("muchos retries ??")
        domains_ko.append(url)
        error_type[url] = "timeout"
    except requests.exceptions.TooManyRedirects:
        print("redirects??")
        error_type[url] = "redirects"
    except requests.exceptions.RequestException as e:
        print("catastrofe")
        error_type[url] = "catastrofe"
        pass
    # catastrophic error. bail.
        #raise SystemExit(e)
    else:
        domains_ok.append(url)
       
    
print(f"Dominios en los que se puede hacer request {domains_ok} vs dominios que NO se puede {domains_ko}")
print(f"errores ---> {error_type}")


