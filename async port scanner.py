"""
Async_port_scanner
"""
import asyncio
import constant
from contextlib import suppress
import time


async def connect_socket(port: int):
    """
    Connect to given IP and port

    :param port: The port for the socket to connect.
    """
    with suppress(Exception):
        await asyncio.open_connection(constant.ip, port)
        print(f"port {port} found!")


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
    await asyncio.gather(*[connect_socket(port)
                           for port in range(constant.start_port, constant.end_port)])


if __name__ == '__main__':
    asyncio.run(main())
