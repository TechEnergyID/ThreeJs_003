import webbrowser
import http.server
import socketserver
import threading
import os
import time

PORT = 8000

def start_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Give the server time to start
time.sleep(1)

# Open the web page
webbrowser.open(f'http://localhost:{PORT}/matrix.html')

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
