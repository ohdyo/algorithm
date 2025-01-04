DROP TABLE IF EXISTS car_region;
DROP TABLE IF EXISTS car_type;
DROP TABLE IF EXISTS race_type;
DROP TABLE IF EXISTS car_monthly;
DROP TABLE IF EXISTS car_data;
DROP TABLE IF EXISTS car_total;

CREATE TABLE car_region (
    region_id INT NOT NULL AUTO_INCREMENT,
    sido_name VARCHAR(50) NOT NULL,
    sigungu_name VARCHAR(50) NULL,
    PRIMARY KEY (region_id)
) ENGINE = INNODB;


CREATE TABLE car_type (
    type_id INT NOT NULL AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (type_id)
) ENGINE = INNODB;


CREATE TABLE race_type (
    race_id INT NOT NULL AUTO_INCREMENT,
    race_name VARCHAR(50) NOT NULL,
    PRIMARY KEY (race_id)
) ENGINE = INNODB;


CREATE TABLE car_monthly (
    monthly_id INT NOT NULL AUTO_INCREMENT,
    month_year VARCHAR(7) NOT NULL,
    PRIMARY KEY (monthly_id)
) ENGINE = INNODB;


CREATE TABLE car_data (
    data_id INT NOT NULL AUTO_INCREMENT,
    region_id INT NOT NULL,
    type_id INT NOT NULL,
    race_id INT NOT NULL,
    monthly_id INT NOT NULL,
    vehicle_count INT NOT NULL,
    PRIMARY KEY (data_id),
    FOREIGN KEY (region_id) REFERENCES car_region(region_id),
    FOREIGN KEY (type_id) REFERENCES car_type(type_id),
    FOREIGN KEY (race_id) REFERENCES race_type(race_id),
    FOREIGN KEY (monthly_id) REFERENCES car_monthly(monthly_id)
) ENGINE = INNODB;


CREATE TABLE car_total (
    total_id INT NOT NULL AUTO_INCREMENT,
    region_id INT NOT NULL,
    race_id INT NOT NULL,
    monthly_id INT NOT NULL,
    total_count INT NOT NULL,
    PRIMARY KEY (total_id),
    FOREIGN KEY (region_id) REFERENCES car_region(region_id),
    FOREIGN KEY (race_id) REFERENCES race_type(race_id),
    FOREIGN KEY (monthly_id) REFERENCES car_monthly(monthly_id)
) ENGINE = INNODB;
