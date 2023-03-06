DROP DATABASE IF EXISTS veterinary_clinic;

CREATE DATABASE veterinary_clinic;

USE veterinary_clinic;

-- Create the Veterinarian table
CREATE TABLE Veterinarian (
    vet_id      INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    dob         DATE NOT NULL,
    gender      VARCHAR(10) NOT NULL,
    degree      VARCHAR(20) NOT NULL,
    phone       VARCHAR(20) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    address     VARCHAR(255) NOT NULL
);

-- Create the Owner table
CREATE TABLE Owner (
    owner_id    INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    phone       VARCHAR(20) NOT NULL,
    email       VARCHAR(255) NOT NULL,
    address     VARCHAR(255) NOT NULL
);

-- Create the Animal table
CREATE TABLE Animal (
    animal_id   INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    species     VARCHAR(255) NOT NULL,
    gender      VARCHAR(10) NOT NULL,
    age         INT NOT NULL,
    weight      DECIMAL(10, 2) NOT NULL,
    owner_id    INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES Owner(owner_id) ON DELETE CASCADE
);

-- Create the Appointment table
CREATE TABLE Appointment (
    appointment_id      INT AUTO_INCREMENT PRIMARY KEY,
    appointment_date    DATETIME NOT NULL,
    animal_id           INT NOT NULL,
    vet_id              INT NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES Animal(animal_id) ON DELETE CASCADE,
    FOREIGN KEY (vet_id) REFERENCES Veterinarian(vet_id) ON DELETE CASCADE
);

-- Create the Medical_Procedure table
CREATE TABLE Medical_Procedure (
    procedure_id    INT AUTO_INCREMENT PRIMARY KEY,
    procedure_name  VARCHAR(255) NOT NULL,
    cost            DECIMAL(10, 2) NOT NULL
);

-- Create the Payment table
CREATE TABLE Payment (
    payment_id      INT AUTO_INCREMENT PRIMARY KEY,
    payment_date    DATE NOT NULL,
    amount          DECIMAL(10, 2) NOT NULL,
    appointment_id  INT NOT NULL,
    procedure_id    INT NOT NULL,
    FOREIGN KEY (appointment_id) REFERENCES Appointment(appointment_id) ON DELETE CASCADE,
    FOREIGN KEY (procedure_id) REFERENCES Medical_Procedure(procedure_id) ON DELETE CASCADE
);
