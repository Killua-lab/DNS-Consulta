import socket

# Solicita ao usuário que insira o domínio alvo
dominio = input("Alvo: ")

# Lista de nomes de host que você deseja verificar
with open('bruteforce.txt', 'r') as arquivo:
    bruteforce = arquivo.readlines()

# Loop pelos nomes de host e tenta obter o endereço IP associado a cada um
for nome in bruteforce:
    DNS = nome.strip('\n') + "." + dominio
    try:
        # Tenta obter o endereço IP associado ao nome de host
        print(DNS , ": " , socket.gethostbyname(DNS))
    except socket.gaierror:
        # Se não for possível resolver o nome de host, passa para o próximo
        pass