CREATE TABLE character (
  character_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  birthDate DATE NOT NULL,
  gender VARCHAR(10) NOT NULL,
  description TEXT
);

CREATE TABLE primoid_category (
  primoid_category_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  rank VARCHAR(1),
  alternate_name VARCHAR(100),
  description TEXT,
  handling TEXT
);

CREATE TABLE primoid_type (
  primoid_type_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  alternate_name VARCHAR(100),
  description TEXT,
  handling TEXT
);

CREATE TABLE primoid (
  primoid_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  alternate_name VARCHAR(100),
  primoid_category_id INT NOT NULL,
  primoid_type_id INT NOT NULL,
  description TEXT,
  FOREIGN KEY (primoid_category_id) REFERENCES primoid_category(primoid_category_id),
  FOREIGN KEY (primoid_type_id) REFERENCES primoid_type(primoid_type_id)
);

CREATE TABLE event (
  event_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  date DATE NOT NULL,
  description TEXT
);

CREATE TABLE relative (
  relative_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  first_character_id INT NOT NULL,
  second_character_id INT NOT NULL,
  first_character_status VARCHAR(100),
  second_character_status VARCHAR(100),
  FOREIGN KEY (first_character_id) REFERENCES character(character_id),
  FOREIGN KEY (second_character_id) REFERENCES character(character_id),
  CONSTRAINT unique_character_pair UNIQUE (first_character_id, second_character_id)
);
