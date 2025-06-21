
# import socket
# import threading

# def receive_messages(conn):
#     while True:
#         try:
#             msg = conn.recv(1024).decode()
#             if msg:
#                 print(f"\nFriend: {msg}\nYou: ", end="")
#         except:
#             print("\n❌ Connection closed.")
#             break

# def send_messages(conn):
#     while True:
#         try:
#             msg = input("You: ")
#             conn.send(msg.encode())
#         except:
#             print("❌ Unable to send message.")
#             break

# def start_peer_chat(mode, host='127.0.0.1', port=5000):
#     if mode == 'server':
#         server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server_socket.bind((host, port))
#         server_socket.listen(1)
#         print(f"🟢 Waiting for connection on {host}:{port}...")
#         conn, addr = server_socket.accept()
#         print(f"✅ Connected to {addr}")
#     else:  # client
#         conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         conn.connect((host, port))
#         print(f"✅ Connected to server at {host}:{port}")

#     threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()
#     send_messages(conn)

# # ---- Execution Example ----
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) < 2:
#         print("Usage:")
#         print("  Server: python chat.py server")
#         print("  Client: python chat.py client <server_ip>")
#     else:
#         mode = sys.argv[1]
#         ip = sys.argv[2] if len(sys.argv) == 3 else '127.0.0.1'
#         start_peer_chat(mode, ip)
