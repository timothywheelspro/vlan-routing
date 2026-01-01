#!/usr/bin/env python3
"""
Simple HTTP server for local portfolio testing.
Usage: python3 server.py [port]
"""

import http.server
import socketserver
import sys
import webbrowser
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    # Change to portfolio directory
    portfolio_dir = Path(__file__).parent
    import os
    os.chdir(portfolio_dir)
    
    Handler = CustomHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/landing.html"
            print(f"\n{'='*60}")
            print(f"Portfolio Server Running")
            print(f"{'='*60}")
            print(f"Local URL: {url}")
            print(f"Serving directory: {portfolio_dir}")
            print(f"\nPress Ctrl+C to stop the server")
            print(f"{'='*60}\n")
            
            # Auto-open browser
            webbrowser.open(url)
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Error: Port {PORT} is already in use.")
            print(f"Try: python3 server.py {PORT + 1}")
        else:
            raise

