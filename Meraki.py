import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

baseURL = 'https://api.meraki.com/api/v1'
api_key = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
def get_org():
    url_org = baseURL + "/organizations"
    headers = {
    "X-Cisco-Meraki-API-Key" : api_key,
    "Content-Type" : "application/json"
    }
    send_request = requests.get(url_org, headers=headers, verify=False)
    data = json.dumps(send_request.json(),indent=4)
    # print(data)    
    arr_id = []
    for i in range(0, len(send_request.json())):
        id_org = send_request.json()[i]["id"]
        arr_id.append(id_org)
    # print(arr_id)
    return arr_id

arr_organizationId = get_org()

def get_devices():
    for i in range(0, len(arr_organizationId)):
        url_device = baseURL + '/organizations/' + str(arr_organizationId[i])  + '/inventory/devices'
        # print(url_device)
        headers = {    
            "Content-Type" : "application/json",
            "X-Cisco-Meraki-API-Key" : api_key            
        }
        send_request = requests.get(url_device, headers=headers, verify=False)
        data = send_request.json()
        show_devices = json.dumps(data, indent=4)
        if len(show_devices) > 2:
            # print('{}: '.format(i), len(show_devices),'\n')
            print(show_devices)

def get_devices_null():
    for i in range(0, len(arr_organizationId)):
        url_device = baseURL + '/organizations/' + str(arr_organizationId[i])  + '/inventory/devices'
        # print(url_device)
        headers = {    
            "Content-Type" : "application/json",
            "X-Cisco-Meraki-API-Key" : api_key            
        }
        send_request = requests.get(url_device, headers=headers, verify=False)
        data = send_request.json()
        show_devices = json.dumps(data, indent=4)
        if len(show_devices) <= 2:
            # print('{}: '.format(i), len(show_devices),'\n')
            print(show_devices) 

get_devices_null()