import http.server
import socketserver
import os
import sys

PORT = int(os.getenv("WEBGL_PORT", "8085"))
DIRECTORY = os.path.join(os.path.dirname(__file__), "Builds", "CipherCourt_WebGL")

class WebGLRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable cache during rapid iterations
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        # Cross-Origin Isolation headers for high-performance WebAssembly
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.wasm'):
            return 'application/wasm'
        if path.endswith('.data'):
            return 'application/octet-stream'
        if path.endswith('.js'):
            return 'application/javascript'
        if path.endswith('.symbols.json'):
            return 'application/json'
        return super().guess_type(path)

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        print(f"[ERROR] Directory does not exist yet: {DIRECTORY}")
    print(f"==================================================")
    print(f" CIPHER COURT - LIVE WEBGL SERVER                 ")
    print(f"==================================================")
    print(f"Serving: {DIRECTORY}")

    server = None
    port_candidates = [PORT] + [p for p in [8085, 8090, 8888, 9090, 8080] if p != PORT]
    for p in port_candidates:
        for host in ["127.0.0.1", "0.0.0.0"]:
            try:
                server = ThreadedHTTPServer((host, p), WebGLRequestHandler)
                PORT = p
                print(f"Server successfully bound to http://{host}:{PORT}")
                break
            except Exception:
                continue
        if server:
            break

    if not server:
        print("[ERROR] Could not bind server to any candidate port.")
        sys.exit(1)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
