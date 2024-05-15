
INSERT INTO Customer (CustomerID, Name, Email, PhoneNumber, Address, CreditScore)
VALUES
    (1, 'John Doe', 'john@example.com', '1234567890', '123 Main St, Anytown, USA', 750),
    (2, 'Jane Smith', 'jane@example.com', '9876543210', '456 Elm St, Springfield, USA', 800),
    (3, 'Rahul Gupta', 'rahul@example.com', '1122334455', '789 Oak St, Mumbai, India', 700),
    (4, 'Amit Patel', 'amit@example.com', '9988776655', '456 Park St, Delhi, India', 720),
    (5, 'Emily Johnson', 'emily@example.com', '5544332211', '789 Cedar St, Los Angeles, USA', 780),
    (6, 'Priya Singh', 'priya@example.com', '6677889900', '890 Maple St, Bangalore, India', 760),
    (7, 'Michael Brown', 'michael@example.com', '8899776655', '987 Pine St, New York, USA', 740),
    (8, 'David Williams', 'david@example.com', '3322114455', '234 Walnut St, Chicago, USA', 790),
    (9, 'Sneha Sharma', 'sneha@example.com', '1122336655', '345 Birch St, Pune, India', 730),
    (10, 'Sarah Miller', 'sarah@example.com', '5566778899', '678 Spruce St, Houston, USA', 770);


INSERT INTO Loan (LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus)
VALUES
    (1, 1, 50000, 5, 24, 'HomeLoan', 'Pending'),
    (2, 2, 75000, 4.5, 36, 'CarLoan', 'Pending'),
    (3, 3, 60000, 5.5, 48, 'HomeLoan', 'Pending'),
    (4, 4, 80000, 4, 24, 'CarLoan', 'Pending'),
    (5, 5, 70000, 4.75, 36, 'HomeLoan', 'Pending'),
    (6, 6, 55000, 6, 48, 'CarLoan', 'Pending'),
    (7, 7, 65000, 4.25, 24, 'HomeLoan', 'Pending'),
    (8, 8, 90000, 3.75, 36, 'CarLoan', 'Pending'),
    (9, 9, 62000, 5.25, 48, 'HomeLoan', 'Pending'),
    (10, 10, 78000, 4.1, 24, 'CarLoan', 'Pending');


INSERT INTO HomeLoan (LoanID, PropertyAddress, PropertyValue)
VALUES
    (1, '123 Main St, Anytown, USA', 200000),
    (3, '789 Oak St, Mumbai, India', 150000),
    (5, '789 Cedar St, Los Angeles, USA', 220000),
    (7, '987 Pine St, New York, USA', 300000),
    (9, '345 Birch St, Pune, India', 180000);


INSERT INTO CarLoan (LoanID, CarModel, CarValue)
VALUES
    (2, 'Toyota Camry', 25000),
    (4, 'Honda Accord', 30000),
    (6, 'Ford Mustang', 40000),
    (8, 'Chevrolet Silverado', 35000),
    (10, 'Tesla Model 3', 60000);
