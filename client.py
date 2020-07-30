import socket
import threading
import base64

passkey = input("Enter your accesskey: ")
PORT= 5050
SERVER = decode_key(passkey)
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect to the socket
client.connect(ADDR)

def decode_key(valu):
    decoded_data = base64.b64decode(valu)
    dec_ip = decoded_data.decode('utf-8')
    if len(dec_ip) == 7:
        dec_ip = '192.168.'+ dec_ip.lstrip('0')
    elif len(dec_ip) == 15:
        dec_ip = dec_ip.lstrip('0')
    else:
        print("Incorrect access key")
    return dec_ip

def send(message_val):
    message = message_val.encode(FORMAT)
    message_length = len(message)
    send_len = str(message_length).encode(FORMAT)
    #padd it to header
    send_len+= b' '*(HEADER-len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))


send("Hello")
send("Peter Kavinsky")
send("Jacob Elordi")
send("aaa")
send("ooo")
#Disconnect
send("!DISCONNECT")

