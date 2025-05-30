import socket
import json
from data_storage import insert_log, create_db

def start_server(host='0.0.0.0', port=5001):
    create_db()  # Ensure the database is initialized
    print(f"[AGGREGATOR] Listening on {host}:{port}...")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    while True:
        client_socket, address = server_socket.accept()
        print(f"[RECEIVED] Connection from {address}")

        data = client_socket.recv(4096).decode()
        try:
            parsed_data = json.loads(data)
            insert_log(parsed_data)
            print("[OK] Data stored:", parsed_data)
        except Exception as e:
            print("[ERROR] Invalid data or failed to insert:", e)

        client_socket.close()

if __name__ == "__main__":
    start_server()
