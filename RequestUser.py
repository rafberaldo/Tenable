import requests
url = "https://10.190.38.40/rest/user"
querystring = 
{"fields":"id,username,locked,authType,role,locked,createdTime,group","":""}
payload = ""
headers = {
 'cookie': "TNS_SESSIONID=01700a09687c64eb4eee08e4b76f47a8",
 'x-apikey': "accesskey=d2ffdb13f78e4d008615d8be368d9739; 
secretkey=b7748a7484fe4da6a6ced55e33b2b43c"
 }
response = requests.request("GET", url, data=payload, headers=headers, 
params=querystring)
print(response.text)