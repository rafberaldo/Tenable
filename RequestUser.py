import requests
url = "https://10.190.38.40/rest/user"
querystring = 
{"fields":"id,username,locked,authType,role,locked,createdTime,group","":""}
payload = ""
headers = {
 'cookie': "TNS_SESSIONID=55668811",
 'x-apikey': "aadddddddd; 
secretkey=aaaaaaa"
 }
response = requests.request("GET", url, data=payload, headers=headers, 
params=querystring)
print(response.text)