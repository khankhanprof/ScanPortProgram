import socket
t_host=str(input("enter host name : "))
t_ip=socket.gethostbyname(t_host)
print(t_ip)
while True:
    t_port=int(input("enter port number: "))
    try:
        sock=socket.socket()
        res=sock.connect((t_ip,t_port))
        print(f"port{t_port} connected")
        sock.close()
    except:
        print(f"port{t_port} not connected")
print("port scanning complete")