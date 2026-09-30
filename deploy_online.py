import subprocess
import time
import re
import os
import sys

# Ensure UTF-8 across Windows terminals
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

PORT = int(os.getenv("WEBGL_PORT", "8085"))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUDFLARED_BIN = os.path.join(ROOT_DIR, "cloudflared.exe")

def start_backend_server():
    backend_script = os.path.join(ROOT_DIR, "Backend", "server.py")
    if os.path.exists(backend_script):
        return subprocess.Popen([sys.executable, backend_script])
    return None

def start_webgl_server():
    server_script = os.path.join(ROOT_DIR, "serve_webgl.py")
    env = os.environ.copy()
    env["WEBGL_PORT"] = str(PORT)
    return subprocess.Popen([sys.executable, server_script], env=env)

def run_deployment():
    print("=" * 65)
    print("   CIPHER COURT: LIVE ONLINE CLOUDFLARE DEPLOYMENT")
    print("=" * 65)

    print(f"[*] Starting local WebGL HTTP server on port {PORT}...")
    server_proc = start_webgl_server()

    print("[*] Starting local Telemetry & Audit Backend server on port 8000...")
    backend_proc = start_backend_server()
    time.sleep(2)

    print(f"[*] Establishing high-speed Cloudflare Tunnel to port {PORT}...")
    cmd = [
        CLOUDFLARED_BIN,
        "tunnel",
        "--protocol", "http2",
        "--url", f"http://127.0.0.1:{PORT}"
    ]

    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            encoding='utf-8',
            errors='replace'
        )

        live_url = None
        for line in proc.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()

            # Search for https://*.trycloudflare.com
            match = re.search(r'(https://[a-zA-Z0-9\.\-_]+\.trycloudflare\.com)', line)
            if match and not live_url:
                live_url = match.group(1)
                url_file = os.path.join(ROOT_DIR, "LIVE_URL.txt")
                with open(url_file, "w", encoding="utf-8") as f:
                    f.write(live_url + "\n")

                print("\n" + "=" * 65)
                print(f"🎉 SUCCESS! CIPHER COURT IS LIVE WORLDWIDE!")
                print(f"🌍 LIVE PUBLIC URL: {live_url}")
                print(f"🎮 Local WebGL URL: http://localhost:{PORT}")
                print(f"📊 Backend Dashboard: http://localhost:8000")
                print(f"🎮 Anyone on any browser anywhere in the world can now play!")
                print(f"💾 Saved to: LIVE_URL.txt")
                print("=" * 65 + "\n")

        proc.wait()
    except KeyboardInterrupt:
        print("\nStopping services...")
    finally:
        if server_proc:
            try:
                server_proc.terminate()
            except Exception:
                pass
        if backend_proc:
            try:
                backend_proc.terminate()
            except Exception:
                pass

if __name__ == "__main__":
    run_deployment()
