CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS 'uuid-ossp';

CREATE TABLE note_content 
(
    note_id UUID PRIMARY KEY REFERENCES note_metadata(id) ON DELETE CASCADE, 
    content text,
);

CREATE TABLE note_metadata
(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    content_id bigserial
    user_id integer NOT NULL, 
    date_added timestamp,
    date_updated timestamp,
    -- site_url text,
    -- context_descriptor text,
    content_format text DEFAULT 'markdown'
    embedding vector(512)
);

CREATE TABLE users
(
    id serial PRIMARY KEY,
    username text UNIQUE,
    password_salt VARCHAR(255),
    password_hash VARCHAR(255)
)
-- CREATE TABLE user_bigtext
-- (
-- id bigserial PRIMARY KEY, 
-- user_id integer NOT NULL, 
-- embedding vector(3),
-- date_added timestamp,
-- datapath text NOT NULL
-- );