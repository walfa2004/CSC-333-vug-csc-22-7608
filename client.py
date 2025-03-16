import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the server. Type 'exit' to quit.")

    while True:
        # Send message to server
        client_message = input("Client: ")
        client_socket.send(client_message.encode())

        if client_message.lower() == "exit":
            break

        # Receive response from server
        server_response = client_socket.recv(1024).decode()
        print(f"Server: {server_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()

