CREATE TABLE movements(
    ID SERIAL PRIMARY KEY,
    brand TEXT,
    model TEXT,
    type_ ENUM('Automatic', 'Manual Mechanical', 'Quartz', 'Mecaquartz'), --Movement type (e.g., “Quartz”, “Automatic”)
    price REAL, --check
    image_url TEXT,
    power_reserve TEXT, --e.g., “40 hours”
    accuracy TEXT, --optional
    description TEXT,     
);

CREATE TABLE cases(
    ID SERIAL PRIMARY KEY,
    brand TEXT,
    model TEXT,
    price REAL, --check
    image_url TEXT,
    material TEXT, --e.g., "316L Stainless Steel"
    dimension1 REAL,
    dimension2 REAL,
    dimension3 REAL,
    description TEXT,     
);

