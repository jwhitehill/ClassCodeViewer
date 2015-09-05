import SimpleHTTPServer
import json
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
		if requestType == "send":
			clientIP = self.client_address[0]
			code = request['code']
			userCodeMap[clientIP] = code
			self.wfile.write("true")
		elif requestType == "receive":
			self.wfile.write(json.dumps(userCodeMap))

if __name__ == "__main__":
	Handler = MyHandler
	httpd = SocketServer.TCPServer(("", PORT), Handler)
	print "serving at port", PORT
	httpd.serve_forever()
