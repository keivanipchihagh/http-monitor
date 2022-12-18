CREATE SCHEMA IF NOT EXISTS http_monitor;

CREATE TABLE IF NOT EXISTS http_monitor.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(60) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS http_monitor.monitors (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    threshold INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    user_id INTEGER NOT NULL REFERENCES http_monitor.users(id)     -- Foreign key
);

CREATE TABLE IF NOT EXISTS http_monitor.requests (
    id SERIAL PRIMARY KEY,
    status_code INTEGER NOT NULL,
    response_time INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    monitor_id INTEGER NOT NULL REFERENCES http_monitor.monitors(id) -- Foreign key
);