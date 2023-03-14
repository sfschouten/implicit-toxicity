CREATE TABLE span_data(
    sample_id VARCHAR PRIMARY KEY,
    dataset_key VARCHAR,
    split VARCHAR,
    full_text VARCHAR,
    toxic BOOLEAN,
    toxic_mask BOOLEAN[],
    toxic_tokens VARCHAR[],
);


