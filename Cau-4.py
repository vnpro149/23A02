#from urllib import response
import requests
import json

requests.packages.urllib3.disable_warnings()

baseUrl = "https://api.meraki.com/api/v1"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
def get_org():
    url = baseUrl + "/organizations"
    
    
    header = {
        "X-Cisco-Meraki-API-Key": api_key,
        "Content-Type" : "application/json"
    }
    
    response = requests.get (url, headers=header, verify=False)
    send_request = requests.get(url_org, headers=headers, verify=False)
    data = json.dumps(send_request.json(),indent=4)
    print(data)
    id_org = send_request.json()[0]["id"]
    # print(data)
    return id_org
get_org()