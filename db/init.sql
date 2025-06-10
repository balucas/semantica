CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE user_text 
(
id bigserial PRIMARY KEY, 
user_id integer NOT NULL, 
context_reference bigserial
embedding vector(3),
date_added timestamp,
actual_data text NOT NULL
);

CREATE TABLE metadata_and_context
(
id bigserial PRIMARY KEY,
date_added timestamp,
site_url text,
context_descriptor text NOT NULL,
embedding vector(3)

)
CREATE TABLE user_bigtext
(
id bigserial PRIMARY KEY, 
user_id integer NOT NULL, 
embedding vector(3),
date_added timestamp,
datapath text NOT NULL
);