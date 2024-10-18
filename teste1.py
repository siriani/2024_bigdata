print("teste teste")
#código para mostrar o ip qual o meu ip?
import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)

#código para mostrar o meu ip publico?
import requests
ip = requests.get('https://api.ipify.org').text
print('My public IP address is:', ip)

#criar um http server para mostrar o diretorio
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()



