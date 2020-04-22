"""
Synchronized port scanner.
"""

from socket import socket, AF_INET, SOCK_STREAM
import time


def connect_socket(guest: socket, ip: str, port: int):
    """
    Connect given socket to given ip and port

   :param guest: The socket to connect.
   :param ip: The ip for the socket to connect.
   :param port: The port for the socket to connect.
    """
    try:
        guest.connect((ip, port))
        print(f"port {port} found")
    except ConnectionError:
        print("connection failed!")


def time_measure(func):
    """
    Measure time for execution

    :param func: The function to be measured.
    """
    def wrapper(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        print(f"{end_time - start_time} seconds took!")
        return func
    return wrapper


@time_measure
def main():
    """
    Execute connect_socket method through many ports with unused sockets
    synchronously
    """
    for i in range(1, 1000):
        s = socket(AF_INET, SOCK_STREAM)
        connect_socket(s, "127.0.0.1", i)


if __name__ == '__main__':
    main()
