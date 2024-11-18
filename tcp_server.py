# Donald Larson
# CIS256 Fall 2024
# EX8 (EX8)
'''
This code, tcp_server.py, implements the server functions of the exercise
described below.

In this exercise, you will create a simple TCP client-server application using
Python. You will:

 - Build a TCP server that listens for incoming connections.
 - Develop a TCP client that connects to the server, sends a message, and
   receives a response.
 - Implement basic error handling to manage common network issues.

Part 1: Create a TCP Server

1. Server Setup:
 - Write a Python script to create a TCP server.
 - The server should listen on a specified port and accept incoming connections
from clients.

2. Sending and Receiving Messages:
 - Once a client connects, the server should be able to send and receive
   messages.

3. Error Handling:
 - Add basic exception handling to manage common network errors.

For this implementation I elected to have the server perform the service of
reversing the text of the input message and sending it back to the client.
The client will send multiple messages and verify that each of the responses are
reversed copies of the message sent as expected.

GitHub repository: https://github.com/DLarsonGH/cse256_EX8
'''
# TCP Server Example

import socket


def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port to listen on
    host = 'localhost'  # Local machine
    port = 12345  # Port number

    # Bind the socket to the address and port
    server_socket.bind((host, port))
    print(f"server: started on {host}:{port}")

    # Listen for incoming connections
    server_socket.listen(1)
    print("server: waiting for a connection...")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"server: connected to {addr}...")
    # Initialize message counter
    msg_count = 0
    try:
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            msg_count += 1
            message_in = data.decode()
            print(f">> Message {msg_count} received:")
            print(f">>\t[{message_in}]")

            # Reverse the text and send in back to the client
            response = message_in[::-1]
            conn.sendall(response.encode())
    except Exception as e:
        print(f"server: An error occurred: {e}")
    finally:
        # Close the connection
        print("server: closing the connection...")
        conn.close()
        print("server: closing the socket...")
        server_socket.close()


if __name__ == "__main__":
    start_server()
