from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "localhost"
PORT = 8000

class KSHTTP(BaseHTTPRequestHandler):
   def do_GET(self):
      self.send_response(200)
      self.send_header("Contend-type", "text/html")
      self.end_headers()
   
      self.wfile.write(bytes(f"<html><body><h1>Kazi samir maked  server !</h1></body></html>","utf-8"))
   
   
   def do_POST(self):
      self.send_response(200)
      self.send_header("Contend-type","application/json")
      self.end_headers()

      date = time.strftime("%Y-%m-%d-%H:%H:%S",time.localtime(time.time()))
      self.wfile.write(bytes('{"time": "'+ date +'"}',"utf=8"))

server = HTTPServer((HOST, PORT), KSHTTP)
print("Server is now runing in port 8000.....")

server.serve_forever()
server.server_close()
print('server is stoped.')
