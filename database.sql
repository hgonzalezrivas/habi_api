SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE IF NOT EXISTS ta_user(
    id              INT AUTO_INCREMENT,
    name            VARCHAR(25) NOT NULL,
    username        VARCHAR(25) NOT NULL UNIQUE,
    password        VARCHAR(16) NOT NULL,
    email           VARCHAR(50) NOT NULL UNIQUE,
    phone_number    VARCHAR(12) NOT NULL UNIQUE,
    birthdate       DATE NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT user_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ta_houses(
    id              INT AUTO_INCREMENT,
    address         VARCHAR(75) NOT NULL,
    city            INT NOT NULL,
    state           INT NOT NULL,
    country         INT NOT NULL,
    status          INT NOT NULL,
    year            VARCHAR(4) NOT NULL,
    price           VARCHAR(10) NOT NULL,
    price           VARCHAR(10) NOT NULL,
    description     VARCHAR(100) NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT house_pk
        PRIMARY KEY (id),
    CONSTRAINT house_city_fk
        FOREIGN KEY (city)
            REFERENCES ta_city (id),
    CONSTRAINT house_state_fk
        FOREIGN KEY (state)
            REFERENCES ta_state (id),
    CONSTRAINT house_country_fk
        FOREIGN KEY (country)
            REFERENCES ta_country (id),
    CONSTRAINT house_status_fk
        FOREIGN KEY (status)
            REFERENCES ta_status (id)
);

CREATE TABLE IF NOT EXISTS ta_city(
    id              INT AUTO_INCREMENT,
    short_name      VARCHAR(10) NOT NULL,
    name            VARCHAR(25) NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT city_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ta_state(
    id              INT AUTO_INCREMENT,
    short_name      VARCHAR(10) NOT NULL,
    name            VARCHAR(25) NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT state_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ta_country(
    id              INT AUTO_INCREMENT,
    short_name      VARCHAR(10) NOT NULL,
    name            VARCHAR(25) NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT country_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ta_status(
    id              INT AUTO_INCREMENT,
    name            VARCHAR(10) NOT NULL,
    description     VARCHAR(30) NOT NULL,
    enabled         INT NOT NULL,
    created_by      VARCHAR(25) NOT NULL,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT status_pk
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS ta_house_reaction(
    id              INT AUTO_INCREMENT,
    house_id        INT NOT NULL,
    user_id         INT NOT NULL,
    CONSTRAINT house_reaction_pk
        PRIMARY KEY (id),
    CONSTRAINT house_id_fk
        FOREIGN KEY (house_id)
            REFERENCES ta_houses (id),
    CONSTRAINT user_id_fk
        FOREIGN KEY (user_id)
            REFERENCES ta_user (id),
);


