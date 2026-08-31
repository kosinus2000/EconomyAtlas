CREATE TABLE voivodeship
(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    area NUMERIC(15,2),
    population INTEGER,
    pkb NUMERIC(15, 2)
);

CREATE TABLE powiat
(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    region_id INTEGER NOT NULL REFERENCES voivodeship(id),
    name VARCHAR(50) NOT NULL,
    area NUMERIC(15,2),
    population INTEGER,
    pkb NUMERIC(15, 2),
    UNIQUE (region_id, name)
);

CREATE TABLE gmina
(
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
    powiat_id INTEGER NOT NULL REFERENCES powiat(id)
    , area_type VARCHAR(30)
    , latitude NUMERIC(9,6),
    longitude NUMERIC(9,6)
    , name VARCHAR(50) NOT NULL
    ,area NUMERIC(15,2),
    population INTEGER,
    pkb NUMERIC(15, 2),
    UNIQUE (powiat_id, name)
)