"""
Synchronized_port_scanner
"""
import constant
from contextlib import suppress
from socket import AF_INET, socket, SOCK_STREAM
import time


def connect_socket(guest: socket, port: int):
    """
    Connect a given socket to a given ip and port

   :param guest: The socket to connect.
   :param port: The port for the socket to connect.
    """
    with suppress(Exception):
        guest.connect((constant.ip, port))
        print(f"port {port} found")


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
    for port in range(constant.start_port, constant.end_port):
        guest = socket(AF_INET, SOCK_STREAM)
        connect_socket(guest, port)


if __name__ == '__main__':
    main()
