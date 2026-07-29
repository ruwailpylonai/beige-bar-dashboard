#!/usr/bin/env python3
"""Tiny stdlib static server for the Beige Bar dashboard preview. Honors Railway's $PORT."""
import http.server, socketserver, os

PORT = int(os.environ.get("PORT", "8080"))
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # preview: always serve fresh so redeploys are visible immediately
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # quiet


socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Beige Bar preview serving {ROOT} on 0.0.0.0:{PORT}", flush=True)
    httpd.serve_forever()
