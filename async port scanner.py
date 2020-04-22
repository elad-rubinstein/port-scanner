"""
Async port scanner.
"""

import time
import asyncio


async def connect_socket(ip: str, port: int):
    """
    Connect to given IP and port

    :param ip: The ip for the socket to connect.
    :param port: The port for the socket to connect.
    """
    try:
        await asyncio.open_connection(ip, port)
        print(f"port {port} found!")
    except WindowsError:
        print("Connection failed!")


def time_measure(func):
    """
    Measure time for execution of asynchronous method

    :param func: The asynchronous function to be measured.
    """
    async def wrapper(*args, **params):
        start_time = time.time()
        result = await func(*args, **params)
        end_time = time.time()
        print(f"{end_time - start_time} seconds took!")
        return result
    return wrapper


@time_measure
async def main():
    """
    Execute connect_socket method through many ports asynchronously
    """
    await asyncio.gather(*[connect_socket("127.0.0.1", i)
                           for i in range(1, 500)])


if __name__ == '__main__':
    asyncio.run(main())
