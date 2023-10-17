import requests

BASE_URL = 'https://api.meraki.com/api/v1'
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

def get(url):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    payload = None
    return requests.get(url, headers=headers, data=payload)

def get_organizations():
    res = get(f'{BASE_URL}/organizations')
    return res.json()

def get_organization_id(index):
    res = get_organizations()
    return res[index]['id']

def get_organization_inventory_devices(organization_id):
    res = get(f'{BASE_URL}/organizations/{organization_id}/inventory/devices')
    return res.json()

def get_devices_with_network_id_as_null():
    organizations = get_organizations()
    devices_with_network_as_null = []
    for organization in organizations:
        print(f"Organization ID: {organization['id']}")
        try: 
            devices = get_organization_inventory_devices(organization['id'])
            for device in devices:
                if not device['networkId'] or device['networkId'] == '':
                    print(f"Serial: {device['serial']}")
                    devices_with_network_as_null.append(device['serial'])
        except Exception as e:
            print(e)
            print(f"Devices: {devices}")
            continue
    print(f'List of devices with network id as null: {devices_with_network_as_null}')

if __name__ == '__main__':
    get_devices_with_network_id_as_null()
