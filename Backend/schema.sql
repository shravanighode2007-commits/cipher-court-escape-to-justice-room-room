CREATE DATABASE cipher_court;
-- Connect to cipher_court, then run:
CREATE TABLE IF NOT EXISTS game_events (
    id SERIAL PRIMARY KEY,
    session_id TEXT NOT NULL,
    scene TEXT NOT NULL,
    event_type TEXT NOT NULL,
    result TEXT NOT NULL,
    details TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
