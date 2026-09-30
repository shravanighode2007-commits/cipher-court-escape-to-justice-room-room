import http.server
import socketserver
import json
import sqlite3
import os
import sys
from datetime import datetime

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8000"))
DB_FILE = os.path.join(os.path.dirname(__file__), "cipher_court.db")

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            scene TEXT NOT NULL,
            event_type TEXT NOT NULL,
            result TEXT NOT NULL,
            details TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

HTML_DASHBOARD = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cipher Court // Database Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Outfit', sans-serif; background: #07090e; color: #e2e8f0; padding: 24px; }
        .container { max-width: 1200px; margin: 0 auto; }
        header { display: flex; justify-content: space-between; align-items: center; padding-bottom: 20px; border-bottom: 1px solid #1e293b; margin-bottom: 24px; }
        h1 { font-size: 28px; color: #fbbf24; font-weight: 700; letter-spacing: 1px; }
        .badge { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid #2563eb; padding: 6px 14px; borderRadius: 20px; font-size: 13px; font-weight: 600; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-bottom: 32px; }
        .stat-card { background: #0f172a; border: 1px solid #1e293b; border-radius: 12px; padding: 20px; }
        .stat-card .label { font-size: 13px; color: #94a3b8; font-weight: 600; text-transform: uppercase; margin-bottom: 6px; }
        .stat-card .value { font-size: 32px; color: #f8fafc; font-weight: 700; }
        .card { background: #0f172a; border: 1px solid #1e293b; border-radius: 12px; padding: 24px; }
        .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
        .card-title { font-size: 18px; color: #f8fafc; font-weight: 600; }
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th { background: #1e293b; color: #94a3b8; padding: 12px 16px; font-size: 13px; font-weight: 600; text-transform: uppercase; }
        td { padding: 14px 16px; border-bottom: 1px solid #1e293b; font-size: 14px; }
        tr:hover { background: rgba(30, 41, 59, 0.5); }
        .tag { display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: 600; }
        .tag-success { background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); }
        .tag-error { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }
        .tag-info { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>CIPHER COURT // DATABASE DASHBOARD</h1>
            <div class="badge">SYSTEM ONLINE // PORT 8000</div>
        </header>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="label">Total Events</div>
                <div class="value" id="stat-events">0</div>
            </div>
            <div class="stat-card">
                <div class="label">Clues Collected</div>
                <div class="value" id="stat-clues">0</div>
            </div>
            <div class="stat-card">
                <div class="label">Puzzles Solved</div>
                <div class="value" id="stat-solved">0</div>
            </div>
        </div>

        <div class="card">
            <div class="card-header">
                <div class="card-title">Live Event Audit Log</div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>#ID</th>
                        <th>Timestamp</th>
                        <th>Scene</th>
                        <th>Event Type</th>
                        <th>Result</th>
                        <th>Details</th>
                    </tr>
                </thead>
                <tbody id="event-table">
                    <tr><td colspan="6" style="text-align:center; color:#64748b;">Loading database events...</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
        async function fetchEvents() {
            try {
                const res = await fetch('/game-events');
                const data = await res.json();
                if (!data.success) return;
                const events = data.events;
                
                document.getElementById('stat-events').innerText = events.length;
                document.getElementById('stat-clues').innerText = events.filter(e => e.event_type === 'clue_collected').length;
                document.getElementById('stat-solved').innerText = events.filter(e => e.event_type === 'puzzle_answer' && e.result === 'correct').length;

                const tbody = document.getElementById('event-table');
                if (events.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center; color:#64748b;">No database events recorded yet. Play the game to generate events!</td></tr>';
                    return;
                }

                tbody.innerHTML = events.map(e => {
                    let tagClass = e.result === 'correct' || e.result === 'started' || e.result === 'success' ? 'tag-success' : (e.result === 'incorrect' || e.result === 'failed' ? 'tag-error' : 'tag-info');
                    return `<tr>
                        <td>#${String(e.id).padStart(3, '0')}</td>
                        <td style="color:#94a3b8;">${e.created_at}</td>
                        <td style="font-weight:600;">${e.scene}</td>
                        <td style="color:#cbd5e1;">${e.event_type}</td>
                        <td><span class="tag ${tagClass}">${e.result}</span></td>
                        <td style="color:#94a3b8;">${e.details || '-'}</td>
                    </tr>`;
                }).join('');
            } catch (err) {
                console.error(err);
            }
        }
        fetchEvents();
        setInterval(fetchEvents, 2000);
    </script>
</body>
</html>"""

class DatabaseRequestHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Quiet logging

    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With')

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_DASHBOARD.encode('utf-8'))
        elif self.path == '/health':
            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "service": "cipher-court-sqlite", "status": "online"}).encode('utf-8'))
        elif self.path.startswith('/game-events'):
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT id, session_id, scene, event_type, result, details, created_at FROM game_events ORDER BY id DESC LIMIT 100")
            rows = cursor.fetchall()
            conn.close()

            events = [{
                "id": r[0], "session_id": r[1], "scene": r[2],
                "event_type": r[3], "result": r[4], "details": r[5],
                "created_at": r[6]
            } for r in rows]

            self.send_response(200)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "events": events}).encode('utf-8'))
        else:
            self.send_response(404)
            self._send_cors_headers()
            self.end_headers()

    def do_POST(self):
        if self.path == '/game-events':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode('utf-8'))
                session_id = data.get('session_id', 'unknown')
                scene = data.get('scene', 'unknown')
                event_type = data.get('event_type', 'unknown')
                result = data.get('result', 'unknown')
                details = data.get('details', '')
                created_at = data.get('created_at', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                conn = sqlite3.connect(DB_FILE)
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO game_events (session_id, scene, event_type, result, details, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (session_id, scene, event_type, result, details, created_at))
                conn.commit()
                event_id = cursor.lastrowid
                conn.close()

                self.send_response(200)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "event_id": event_id}).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self._send_cors_headers()
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self._send_cors_headers()
            self.end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == "__main__":
    init_db()
    display_host = "127.0.0.1" if HOST == "0.0.0.0" else HOST
    print(f"[CIPHER COURT] Database Web Server online!")
    print(f"  -> Dashboard & API: http://{display_host}:{PORT}")
    print(f"  -> Health Check:    http://{display_host}:{PORT}/health")
    print(f"  -> Live Events:     http://{display_host}:{PORT}/game-events")
    server = ThreadedHTTPServer((HOST, PORT), DatabaseRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.shutdown()
        server.server_close()
        print("Server stopped cleanly.")
