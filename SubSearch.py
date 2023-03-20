import socket
import subprocess

domain = input("Ingrese el nombre de dominio principal: ")

subdomains = ["www", "mail", "blog", "ftp", "webmail", "forum"]

for subdomain in subdomains:
    try:
        host = f"{subdomain}.{domain}"
        ip = socket.gethostbyname(host)

        print(f"Subdominio encontrado: {host} ({ip})")

    except:
        pass