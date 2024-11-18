# Donald Larson
# CIS256 Fall 2024
# EX8 (EX8)
'''
This code, tcp_client.py, implements the client functions of the exercise
described below.

In this exercise, you will create a simple TCP client-server application using
Python. You will:

 - Build a TCP server that listens for incoming connections.
 - Develop a TCP client that connects to the server, sends a message, and
   receives a response.
 - Implement basic error handling to manage common network issues.

Part 2: Create a TCP Client

Client Setup:

1. Write a Python script to create a TCP client.
 - The client should connect to the server, send a message, and receive a
   response.

2. Testing Communication:
 - Ensure the client can send messages to the server and receive responses
   correctly.

For this implementation I elected to have the server perform the service of
reversing the text of the input message and sending it back to the client.
The client will send multiple messages and verify that each of the responses are
reversed copies of the message sent as expected.

GitHub repository: https://github.com/DLarsonGH/cse256_EX8
'''
# TCP Client Example

import socket

# Test messages to be sent to the server
msgs = ['ABCDEFG123456789',
        'Every good boy deserves favor.',
        'A stitch in time saves nine.']


def verify_response(msg_no, msg_in):
    '''
    Verify that the input message is as expected by reversing its contents
    and comparing the result with the string at msgs[msg_no] (which is the
    message sent to the server).  If the strings match report success, otherwise
    report the failure.
    :param msg_no: Index number of the message sent in the msgs list
    :param msg_in: String containing the response received from the server
    :return: None
    '''
    if msg_in[::-1] == msgs[msg_no]:
        print(f">>Response {msg_no} received and verified:")
        print(f">>\t[{msg_in}]")
    else:
        print(f">>Response {msg_no} received and but NOT verified:")
        print(f">>\t[{msg_in}]")


def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port to connect to
    host = 'localhost'  # Server address
    port = 12345  # Port number
    print(f"client: attempting to connect to {host}:{port}  ...")
    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"client: connected to {host}:{port}  ...")
    except Exception as e:
        # Something is wrong, report and exit.
        print(f"client: An error occurred: {e}")
        exit(1)

    # Loop through the list of messages, sending and verifying each.
    for i, message in enumerate(msgs):
        try:
            # Send a message to the server
            client_socket.sendall(message.encode())

            # Receive a response from the server
            response = client_socket.recv(1024).decode()
            # Verify the contents of the message.
            verify_response(i, response)
        except Exception as e:
            print(f"client: An error occurred: {e}")
            break

    print("client: closing the connection ...")
    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    start_client()
