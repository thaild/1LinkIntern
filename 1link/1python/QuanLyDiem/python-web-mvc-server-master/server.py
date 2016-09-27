#! /usr/local/bin/python3

from http.server import HTTPServer, CGIHTTPRequestHandler
import cgitb; cgitb.enable()
#import sys-bin alias

port = 8080
handler = CGIHTTPRequestHandler
#handler.cgi_directories = ["/home/francesco/webapp/"]
httpd = HTTPServer(('', port), handler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()
