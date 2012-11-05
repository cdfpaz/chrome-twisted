from twisted.internet import reactor
from twisted.web import http
from time import gmtime, strftime

server_requests = {}

class processRequest:
    def __init__(self, userid):
        self.userid = userid
        self.process()

    def process(self):
        self.result = '{ "ack" : "'+ self.userid + '" }'

class RequestHandler(http.Request):
    
    def process(self):
        
        if self.path.startswith('/login'):
            print self.client.host, " initiated login request at: ", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), " with uri:", self.uri

            if '?' in self.uri:
                id = self.uri.split('?', 1)[1]
                if self.client.host in server_requests:
                    if server_requests[self.client.host] != id:
                        return self.finish()
                else:
                    server_requests[self.client.host] = id

                p = processRequest(id)
                self.write( p.result )
                return self.finish()

        self.write( "can I help ya ?" )
        return self.finish()

class Channel(http.HTTPChannel): 
    requestFactory = RequestHandler 
        
class ProxyFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return Channel()

reactor.listenTCP(8088, ProxyFactory())
reactor.run()

