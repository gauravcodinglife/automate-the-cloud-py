from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os
from datetime import datetime

class CloudInfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        env_vars = "\n".join([f"{k}={v}" for k, v in os.environ.items()])

        response = f"""
        ===== Cloud Container Info =====

        Hostname: {hostname}
        IP Address: {ip_address}
        Current Time: {current_time}

        --- Environment Variables ---
        {env_vars}
        """

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(response.encode())

# Run server on port 8000
server = HTTPServer(("0.0.0.0", 8000), CloudInfoHandler)
print("Cloud Info Server running on port 8000...")
server.serve_forever()

