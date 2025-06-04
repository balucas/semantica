CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE user_text 
(
id bigserial PRIMARY KEY, 
user_id integer NOT NULL, 
embedding vector(3),
date_added timestamp,
actual_data text NOT NULL
);

CREATE TABLE user_bigtext
(
id bigserial PRIMARY KEY, 
user_id integer NOT NULL, 
embedding vector(3),
date_added timestamp,
datapath text NOT NULL
);