import socket


dir_path = r"C:\Users\Shahar\Downloads\client_server\server_files"
def luanch_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 1600))
    return s


def main():
    s = luanch_server()
    while True:
        s.listen()
        print("server listening...")
        conn, headers = recv_headers(s)
        headers = headers.split("\r\n") # [method, name, length ]
        method = headers[0]
        if method == "post":
            post(headers, conn)


def post(headers, conn):
    name = headers[1]
    length = headers[2]
    file_path = dir_path + f"\\{name}"
    con = conn.recv(length).decode()
    f1 = open(file_path, 'wb')
    f1.write(con)
    f1.close()
    conn.send("file uploaded successfully") 




def recv_headers(s):
    conn, addr = s.accept()
    headers = ""
    while headers[-4:] != "\r\n\r\n":
        headers += conn.recv(1).decode()
    return conn, headers


if __name__ == "__main__":
    main()
print("run has complete")