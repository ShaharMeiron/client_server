import socket
import os

def main():
    s = socket.socket()
    s.connect(("127.0.0.1", 1600))
    method = input("what do you want?  get post or exit")
    if method == "post":
        post(s)
        



def post(s):
    path = r"C:\Users\Shahar\Downloads\client_server\client_files\banana.txt" # input("enter the file you'd like to post")
    f1 = open(path, 'wb')
    con = f1.read()
    f1.close()
    length = str(len(con))
    name = os.path.basename(path)
    s.send(f"post\r\n{name}\r\n{length}\r\n\r\n{con}")


if __name__ == "__main__":
    main()