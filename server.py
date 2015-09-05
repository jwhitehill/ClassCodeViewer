import SimpleHTTPServer
from base64 import decodestring
import cgi
import SocketServer

PORT = 8080
userCodeMap = {}

def cgiFieldStorageToDict (fieldStorage):
	"""Get a plain dictionary, rather than the '.value' system used by the cgi module."""
	params = {}
	for key in fieldStorage.keys():
		params[ key ] = fieldStorage[ key ].value
	return params

class MyHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_POST (self):
		form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"})

		request = cgiFieldStorageToDict(form)
		requestType = request["type"]
		print "hi"
		print requestType
		if requestType == "send":
			clientIP = self.client_address[0]
			userCodeMap[clientIP] = request['code']
			print userCodeMap
		elif requestType == "receive":
			print "receive"

		self.wfile.write("true")

Handler = MyHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
