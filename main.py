from socket import socket, gethostbyname, gethostname, AF_INET, SOCK_STREAM
from tkinter import Tk, Frame, Entry, Label, Scrollbar, Button
from threading import Thread
import logging

from abc import ABC, abstractmethod
class AbstractServerClass(ABC):
    ''' 추상클래스 '''
    def __init__(self):
        ...

    @abstractmethod
    def send_data(self, data):
        ''' send data method '''
        ...

    @abstractmethod
    def recv_data(self):
        ''' recive data method '''
        ...

class Server(AbstractServerClass):
    def start(self, host: str, port: int, name: str):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()
        self.client, self.addr = self.sock.accept()
        self.client.sendfile(name.encode)
        name = self.client.recv(1024).decode()
        return name
        
    def send_data(self, data):
        if data:
            self.client.send(data.encode())
            return data

    def recv_data(self):
        while 1:
            data = self.client.recv(1024).decode()
            if not data:
                break
            return data

class Client(AbstractServerClass):
    def start(self, host: str, port: int, name: str):
        self.client_sock = socket(AF_INET, SOCK_STREAM)
        self.client_sock.connect(host, port)
        self.client_sock.sendfile(name.encode())
        name = self.client_sock.recv(1024).decode()
        return name
    
if __name__ == "__main__":
    host = gethostbyname(gethostname())
    port = 9063

    server = Server()
    server.start(host=host, port=port, name='hh')
    server.send_data()
    server.recv_data()

    
    client = Client()
    client.connect(host=host, port=port, name='tt')
    client.send_data()
    client.recv_data()