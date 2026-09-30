import os
from datetime import datetime, timezone
from typing import Optional

import psycopg2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/cipher_court"
)

app = FastAPI(title="Cipher Court Database API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GameEvent(BaseModel):
    session_id: str
    scene: str
    event_type: str
    result: str
    details: Optional[str] = ""
    created_at: Optional[str] = None


def get_conn():
    return psycopg2.connect(DATABASE_URL)


def ensure_table():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS game_events (
                    id SERIAL PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    scene TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    result TEXT NOT NULL,
                    details TEXT,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
                )
            """)
        conn.commit()
    finally:
        conn.close()

@app.on_event("startup")
def startup():
    ensure_table()

@app.get("/health")
def health():
    return {"success": True, "service": "cipher-court-db"}

@app.post("/game-events")
def create_event(event: GameEvent):
    created = event.created_at or datetime.now(timezone.utc).isoformat()
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """INSERT INTO game_events
                   (session_id, scene, event_type, result, details, created_at)
                   VALUES (%s, %s, %s, %s, %s, %s)
                   RETURNING id""",
                (event.session_id, event.scene, event.event_type,
                 event.result, event.details, created)
            )
            event_id = cur.fetchone()[0]
        conn.commit()
        return {"success": True, "event_id": event_id}
    finally:
        conn.close()

@app.get("/game-events")
def list_events(limit: int = 100):
    limit = max(1, min(limit, 500))
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """SELECT id, session_id, scene, event_type, result, details, created_at
                   FROM game_events ORDER BY id DESC LIMIT %s""",
                (limit,)
            )
            rows = cur.fetchall()
        return {
            "success": True,
            "events": [
                {
                    "id": r[0], "session_id": r[1], "scene": r[2],
                    "event_type": r[3], "result": r[4], "details": r[5],
                    "created_at": r[6].isoformat()
                } for r in rows
            ]
        }
    finally:
        conn.close()
