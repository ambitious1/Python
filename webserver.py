#!/usr/bin/python

import socket, sys

#config constants
CFG_SRV_BIND_IF = "localhost"
CFG_SRV_BIND_PORT = 8080
CFG_SRV_LISTEN_BACKLOG = 10
#end of config constants

#canned HTTP Response 
HTTP_RESPONSE = """HTTP/1.1 200 OK
Date: Saturday, 20 December 2014 05:03:00 EST
Server: Apache/2.2.17 (Unix) mod ssl/2.2.17 OpenSSL/0.9.8l DAV/2
Last-Modified: Sat, 28 Aug 2010 22:17:02 GMT
Etag: "20e2b8b-3c-48ee99731f380"
Accept-Ranges: bytes
Content-Length: 49
Connection: close
Content-Type: text/html

<html><body><h1>Hello, World!</h1></body></html>
"""

#create a TCP socket to listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prevent from address already in use upon server restart
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind the socket to the port
server_address = (CFG_SRV_BIND_IF, CFG_SRV_BIND_PORT)
print >>sys.stderr, 'our URL is http://localhost:%d/' % server_address[1]
print >>sys.stderr, 'we can only be stopped by CTRL+C'
server.bind(server_address)

#Listen for incoming connections
server.listen(CFG_SRV_LISTEN_BACKLOG)

while True:
    try: #wait for incoming connection
        connection, client_address = server.accept()
        print >>sys.stderr, 'New connection from', client_address

        #dont care what the browser wants we'll just send our response
        connection.send("%s" % HTTP_RESPONSE)
        print >>sys.stderr, 'Response sent.'

        #indicate we are going to disconnect
        connection.shutdown(socket.SHUT_WR | socket.SHUT_RD)

        #and finally we close the connection
        connection.close()
        print >>sys.stderr, 'Connection closed.'
    except:
        #CTRL+C pressed or worse, looks like we're dying
        print "\n *** Ouch, that hurt! ***"
        break
print >>sys.stderr, 'Shutting down...'
server.close()
print >>sys.stderr, 'Last line before exitting. Over and out.'
