create database SuiviTaches;

CREATE TABLE IF NOT EXISTS tTypeProjet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tEtatProjet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    etat varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS tProjets (
    id int NOT NULL AUTO_INCREMENT,
    nom varchar(500) NOT NULL,
    type_id int NOT NULL,
    etat_id int NOT NULL,
    charge double,
    tempsPasse double,
    descriptif text,
    remarque text,
    PRIMARY KEY(id),
    FOREIGN KEY (type_id) 
        REFERENCES tTypeProjet (id) 
        ON UPDATE RESTRICT 
        ON DELETE CASCADE,
    FOREIGN KEY (etat_id) 
        REFERENCES tEtatProjet (id) 
        ON UPDATE RESTRICT 
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tTaches (
    id INT AUTO_INCREMENT,
    date DATETIME NOT NULL,
    projet_id int(10) NOT NULL,
    tempsPasse int(5),
    tempsPrevu int(5),
    Description TEXT,
    PRIMARY KEY(id),
    FOREIGN KEY (projet_id) 
        REFERENCES tProjets (id) 
        ON UPDATE RESTRICT 
        ON DELETE CASCADE
);