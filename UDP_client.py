"""
udp_client.py
Maxmillion Maldonado
-------------
A simple UDP client that:
- Sends data from stdin to a UDP server in fixed-size chunks
- Prints debug info (chunks sent, bytes, throughput)

Usage:
python3 udp_client.py [Server IP] [Server Port] < [filename]
"""

import sys
import socket
import time

SEND_BUFFER_SIZE = 2048  # bytes per chunk


def client(server_ip, server_port):
    """
    Send stdin data to a UDP server in chunks.
    Prints per-chunk debug info and total transfer stats.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            chunk_count = 0
            total_bytes = 0
            start_time = time.perf_counter()

            # Read stdin and send in chunks
            while True:
                data_chunk = sys.stdin.buffer.read(SEND_BUFFER_SIZE)
                if not data_chunk:
                    break

                udp_socket.sendto(data_chunk, (server_ip, server_port))
                chunk_count += 1
                total_bytes += len(data_chunk)
                print(
                    f"[DEBUG] Sent chunk {chunk_count}, {len(data_chunk)} bytes",
                    file=sys.stderr
                )

            # Transfer summary
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(
                f"[DEBUG] Finished sending. Total chunks: {chunk_count}",
                file=sys.stderr
            )
            print(
                f"Sent {total_bytes} bytes in {duration:.2f}s "
                f"({total_bytes / duration / 1024:.2f} KB/s)",
                file=sys.stderr
            )

    except socket.error as e:
        print(f"Socket error: {e}", file=sys.stderr)


def main():
    """Parse command-line arguments and run the UDP client."""
    if len(sys.argv) != 3:
        sys.exit(
            "Executing Command: "
            "python3 udp_client.py [Server IP] [Server Port] < [filename]"
        )

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)


if __name__ == "__main__":
    main()

