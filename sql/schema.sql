
CREATE DATABASE LMSDB;

USE LMSDB;

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(20),
    Address NVARCHAR(255),
    CreditScore INT
);

CREATE TABLE Loan (
    LoanID INT PRIMARY KEY,
    CustomerID INT,
    PrincipalAmount DECIMAL(18, 2),
    InterestRate DECIMAL(5, 2),
    LoanTerm INT,
    LoanType NVARCHAR(50),
    LoanStatus NVARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);


CREATE TABLE HomeLoan (
    LoanID INT PRIMARY KEY,
    PropertyAddress NVARCHAR(255),
    PropertyValue DECIMAL(18, 2),
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);


CREATE TABLE CarLoan (
    LoanID INT PRIMARY KEY,
    CarModel NVARCHAR(100),
    CarValue DECIMAL(18, 2),
    FOREIGN KEY (LoanID) REFERENCES Loan(LoanID)
);

SELECT * FROM Customer;
SELECT * FROM Loan;
SELECT * FROM HomeLoan;
SELECT * FROM CarLoan;
