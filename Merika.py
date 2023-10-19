import requests
import json
requests.packages.urllib3.disable_warnings()

class Meraki():
    def __init__(self,url,apikey):
        self.url=url
        self.apikey=apikey
        self.header={
            'Accept':'application/json',
            'Authorization':'Bearer 6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
        }
    
    def showvalue(self):
        print("URL:",self.url)

    def getOrgID(self):
        urlOrg=self.url+"/organizations"
        
        resp=requests.get(url=urlOrg,headers=self.header,verify=False)
        lorgid=[]
        for i in resp.json():
            lorgid.append(i['id'])
        # print(lorgid)
        # print(resp.json())
        # idOrg=resp.json()[0]['id']
        # return idOrg
        return lorgid
    def getOrginfo(self,id):
        urlOrg=self.url+'/organizations/{}'.format(id)

        resp=requests.get(url=urlOrg,headers=self.header,verify=False)
        print(resp.json())
        

    def getNetwork(self,id):
        urlNet=self.url+'/organizations/{}/networks'.format(id)

        resp=requests.get(url=urlNet,headers=self.header,verify=False)
        print(resp.json())
        # netid=resp.json()[0]['id']
        # return netid
        lnetid=[]
        for i in resp.json():
            lnetid.append(i['id'])
        print(lnetid)
    # def getdevice(self,lid):
    #     print(lid);
    def getDevices(self,lorg):
        # print(lorg)
        # # url_device = url+'/organizations/{}/inventory/devices'.format(lorg[2])
        # url_device = url+'/organizations/'+ '575334852396584362' +'/inventory/devices'
        # send_request = requests.get(url_device, headers=self.header, verify=False)
        # data = send_request.json()
        # print(data)
        lnull=[]
        for i in lorg:
            url_device = url+'/organizations/'+ i +'/inventory/devices'
            send_request = requests.get(url_device, headers=self.header, verify=False)
            data = send_request.json()
            # print(data[])
            show_devices = json.dumps(data,indent=4)
            lnull+=data
            # netid=data[3]['networkId']
            # print(netid)
            #print(show_devices)
        for i in lnull:
            # print(type(i['networkId']))
            try:
                if i['networkId'] == None:
                    print(i)
            except:
                print(i)
        # print(show_devices)
        # serialId = data[0]['serial']
        # print(serialId)


url="https://api.meraki.com/api/v1"
apikey="6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

MRK=Meraki(url=url,apikey=apikey)
# MRK.showvalue()
Lorg=MRK.getOrgID()
# lnetid=MRK.getNetwork(OrgID)
# print(lnetid)
# print(OrgID)
MRK.getDevices(Lorg)
# MRK.getOrginfo(OrgID)