# echothread.py
#
# A concurrent echo server using threads

import socketserver


class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("Connection from", self.client_address)
        while True:
            data = self.request.recv(65536)
            if not data:
                break
            self.request.sendall(data)
        print("Client closed")


class MyServer(socketserver.ThreadingTCPServer):
    request_queue_size = 1024


serv = MyServer(("", 45000), EchoHandler)
# serv = SocketServer.ForkingTCPServer(("",45000),EchoHandler)
serv.serve_forever()
