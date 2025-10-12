"""
udp_server.py
Maxmillion Maldonado
-------------
A simple UDP server that:
- Listens for incoming datagrams from clients
- Receives and writes data to stdout (can redirect to file)
- Prints debug info (bytes received, client address, throughput)

Usage:
python3 udp_server.py [Server Port]

To find server IP:
hostname -I
"""

import sys
import socket
import time

RECV_BUFFER_SIZE = 2048  # bytes per recv call


def server(server_port):
    """
    Start the UDP server and continuously receive data from clients.
    Prints per-chunk debug messages and final stats on shutdown.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            udp_socket.bind(('', server_port))
            print(f"UDP Server listening on port {server_port}...", file=sys.stderr)

            total_bytes = 0
            start_time = time.perf_counter()

            # Continuously receive data
            while True:
                data_received, client_addr = udp_socket.recvfrom(RECV_BUFFER_SIZE)
                if not data_received:
                    continue

                total_bytes += len(data_received)
                sys.stdout.buffer.write(data_received)
                sys.stdout.buffer.flush()
                print(
                    f"[DEBUG] Received {len(data_received)} bytes from {client_addr}",
                    file=sys.stderr
                )

    except KeyboardInterrupt:
        # Show final stats on Ctrl+C shutdown
        end_time = time.perf_counter()
        duration = end_time - start_time
        print("Server shutting down (Ctrl+C).", file=sys.stderr)
        print(
            f"Total received: {total_bytes} bytes in {duration:.2f}s "
            f"({total_bytes / duration / 1024:.2f} KB/s)",
            file=sys.stderr
        )

    except socket.error as e:
        print(f"Socket error: {e}", file=sys.stderr)


def main():
    """Parse command-line argument and start the UDP server."""
    if len(sys.argv) != 2:
        sys.exit("Executing Command: python3 udp_server.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)


if __name__ == "__main__":
    main()

