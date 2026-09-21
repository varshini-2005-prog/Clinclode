CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TYPE document_status AS ENUM (
    'received',
    'processing',
    'ready',
    'failed',
    'quarantined'
);

CREATE TYPE document_type AS ENUM (
    'discharge',
    'radiology',
    'progress'
);

CREATE TABLE IF NOT EXISTS documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    external_ref TEXT,
    doc_type document_type NOT NULL,
    raw_text_encrypted BYTEA,
    deid_text TEXT,
    phi_map_encrypted BYTEA,
    status document_status NOT NULL DEFAULT 'received',
    version INTEGER NOT NULL DEFAULT 1,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_documents_status_created
ON documents(status, created_at);
