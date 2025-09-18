import socket 


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = '192.168.1.1'
    port = 443
    s.connect_ex((host, port))
    banner=s.recv(1024)
    print('Result is {}'.format(banner))
    s.close()


if __name__ == '__main__':
    main()
