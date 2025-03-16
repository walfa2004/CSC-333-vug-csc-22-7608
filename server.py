import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        # Receive message from client
        client_message = client_socket.recv(1024).decode()
        if client_message.lower() == "exit":
            print("Client disconnected.")
            break

        print(f"Client: {client_message}")

        # Send response to client
        server_response = input("Server: ")
        client_socket.send(server_response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
