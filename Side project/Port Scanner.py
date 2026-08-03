import socket
import requests
https = input("entry the url")
socket_url = socket.gethostbyname(https)
socket_url.recv(1024)
for s in range(1,100):
    try:
        response = requests.get(socket_url, timeout=3)
        if socket_url.recv == 0:
            print(f"url = {socket.gethostbyname(https)}")
            print(f"url = {socket.gethostbyname(socket_url)}")
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")