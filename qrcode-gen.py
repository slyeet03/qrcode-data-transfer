import qrcode
import sys
import cv2
import http.server
import socket
import socketserver
import os
from PIL import Image

# Open the QR Code in a window
def open_qrcode():
    img = cv2.imread("qr_code.png", cv2.IMREAD_ANYCOLOR)

    while True:
        cv2.imshow("QR Code", cv2.resize(img, (600, 600)))  # Adjust the size of the window
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
        sys.exit()

# Generate QR Code for urls and links
def links_or_texts(data):
    qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    open_qrcode()    

# Host a server with the path specified by the user and generate QR Code of that link
def files(path):
    hostname = socket.gethostname()    
    IP = socket.gethostbyname(hostname)      
    url = IP + ":" + "8000"

    qr = qrcode.QRCode(version=8, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")

    im = Image.open("qr_code.png")
    im.show()

    # Change the current working directory
    os.chdir(path)

    class CustomHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

    PORT = 8000
    handler = CustomHttpRequestHandler

    server = socketserver.TCPServer(("", PORT), handler)
    print(f"Server started at port {PORT}. Press CTRL+C to close the server.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server Closed")
    
    
def main():
    choice = input("1) Url\n2) Text\n3) Files\n")
    
    if choice == "1":
        data = input("Enter url:\n")
        links_or_texts(data)
    elif choice == "2":
        data = input("Enter text:\n")
        links_or_texts(data)
    elif choice == "3":
        path = input("Enter file path:\n")
        files(path)

if __name__ == "__main__":
    main()