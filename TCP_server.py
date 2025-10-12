"""
tcp_server.py
Maxmillion Maldonado
-------------------
A simple TCP multi-client server:
- Handles multiple clients concurrently using threads
- Receives data from clients and writes to stdout
- Prints debug info (bytes received, duration, throughput) to stderr

Usage:
python3 server-python.py [Server Port]

To find server IP:
hostname -I
"""

import sys
import socket
import threading
import time

RECV_BUFFER_SIZE = 2048  # bytes to read per recv call
QUEUE_LENGTH = 10        # max queued connections


def server(server_port):
    """
    Starts the TCP server and continuously accepts client connections.
    Each client is handled in a separate thread.
    """
    servicing_socket = None  # Ensure proper closure in finally block

    try:
        # Create TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
            listening_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listening_socket.bind(('', server_port))
            listening_socket.listen(QUEUE_LENGTH)
            print(
                "Server waiting for client connections...",
                file=sys.stderr
            )

            # Accept clients continuously
            while True:
                servicing_socket, client_addr = listening_socket.accept()
                # Start a new thread for each client
                worker_thread = threading.Thread(
                    target=serve_client,
                    args=(servicing_socket, client_addr)
                )
                worker_thread.start()

    except KeyboardInterrupt:
        print("Ctrl+C pressed. Server shutting down", file=sys.stderr)

    except socket.error as e:
        print(f"Socket error: {e}", file=sys.stderr)

    finally:
        if servicing_socket:
            servicing_socket.close()


def serve_client(servicing_socket, client_addr):
    """
    Handles a single client connection.
    Receives data in chunks and writes to stdout.
    Prints debug info (bytes received, duration, throughput) to stderr.
    """
    print(f"Client {client_addr} connected.", file=sys.stderr)
    total_bytes = 0
    start_time = time.perf_counter()

    try:
        while True:
            data_received = servicing_socket.recv(RECV_BUFFER_SIZE)
            if not data_received:
                break
            total_bytes += len(data_received)
            sys.stdout.buffer.write(data_received)

        sys.stdout.buffer.flush()

    except socket.error as e:
        print(f"Socket error client {client_addr}: {e}", file=sys.stderr)

    finally:
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(
            f"Received {total_bytes} bytes from {client_addr} in "
            f"{duration:.2f}s ({total_bytes / duration / 1024:.2f} KB/s)",
            file=sys.stderr
        )
        print(f"{client_addr} serviced.", file=sys.stderr)
        servicing_socket.close()

def main():
    """Parse command-line argument and start the server."""
    if len(sys.argv) != 2:
        sys.exit("Executing Command: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()

