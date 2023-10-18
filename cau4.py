import requests

BASE_URL = 'https://api.meraki.com/api/v1'
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

def get(url):
    headers = {
        'Accept': 'application/json',
        'X-Cisco-Meraki-API-Key': API_KEY
    }
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

def get_devices_with_network_id_as_null():
    url = f'{BASE_URL}/organizations'
    organizations = get(url)

    if organizations is None:
        print("Failed to fetch organizations.")
        return

    devices_with_network_as_null = []

    for organization in organizations:
        org_id = organization['id']
        url = f'{BASE_URL}/organizations/{org_id}/inventory/devices'
        devices = get(url)

        if devices is None:
            print(f"Failed to fetch devices for organization {org_id}")
            continue

        for device in devices:
            if not device.get('networkId') or device['networkId'] == '':
                print(f"Serial: {device['serial']}")
                devices_with_network_as_null.append(device['serial'])

    if devices_with_network_as_null:
        print(f'List of devices with network id as null: {devices_with_network_as_null}')
    else:
        print('No devices with network id as null found.')

if __name__ == '__main__':
    get_devices_with_network_id_as_null()

