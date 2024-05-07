# QR Code File Tranfer
This Python script allows you to generate QR codes for URLs, text, or host a local server to share files. The generated QR code is displayed in a window, and in the case of hosting a server, the QR code contains the IP address and port of the local server.

## Prerequisites
- OpenCV
- qrcode
- PIL (Python Imaging Library)

You can install the required packages using pip:
```
pip install opencv-python qrcode pillow
```

## Usage
1. Run the script:
`py qrcode-gen.py`
2. Choose one of the following options:
    1) Url: Enter a URL, and the script will generate a QR code for that URL.
    2) Text: Enter a text string, and the script will generate a QR code for that text.
    3) Files: Enter a file path, and the script will start a local server at http://your-ip-address:8000 and generate a QR code containing the server's URL. Scanning the QR code will open the specified directory in a web browser.
3. The generated QR code will be displayed in a window. Press any key to close the window.
