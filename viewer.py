import httplib
import json
from base64 import decodestring
from server import PORT

httpServ = httplib.HTTPConnection("127.0.0.1", PORT)
httpServ.connect()

httpServ.request("POST", "", "type=receive")

response = httpServ.getresponse()
if response.status == httplib.OK:
    userCodeMap = json.loads(response.read())
    for user in userCodeMap.keys():
	    code = decodestring(userCodeMap[user])
	    print user, code

httpServ.close()
