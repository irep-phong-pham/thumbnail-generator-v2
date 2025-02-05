CREATE DATABASE IF NOT EXISTS app;

CREATE TABLE IF NOT EXISTS app.T_IMAGES (
    id INT NOT NULL AUTO_INCREMENT,
    image_url VARCHAR(255) NOT NULL,
    image_name VARCHAR(255) NOT NULL,
    image_size BIGINT NOT NULL,
    upload_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS app.T_THUMBNAILS (
    id INT NOT NULL AUTO_INCREMENT,
    job_id INT NOT NULL,
    image_id INT NOT NULL,
    thumbnail_url VARCHAR(255) NOT NULL,
    thumbnail_name VARCHAR(255) NOT NULL,
    thumbnail_size BIGINT NOT NULL,
    upload_time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS app.T_JOBS (
    id INT NOT NULL AUTO_INCREMENT,
    image_id INT NOT NULL,
    status ENUM('QUEUED', 'PROCESSING', 'SUCCEEDED', 'FAILED', 'CANCELED') NOT NULL DEFAULT 'QUEUED',
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
