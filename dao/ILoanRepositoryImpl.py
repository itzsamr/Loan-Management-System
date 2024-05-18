from .ILoanRepository import ILoanRepository
from util.DBConnection import DBConnUtil
from exception.InvalidLoanException import InvalidLoanException
from decimal import Decimal
from entity import Customer


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def customer_exists(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT COUNT(1) FROM Customer WHERE CustomerID = ?", (customer_id,)
        )
        exists = cursor.fetchone()[0]
        cursor.close()
        return exists > 0

    def add_customer(self, customer):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Customer (CustomerID, Name, Email, PhoneNumber, Address, CreditScore) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    customer.customer_id,
                    customer.name,
                    customer.email,
                    customer.phone_number,
                    customer.address,
                    customer.credit_score,
                ),
            )
            self.connection.commit()
        except Exception as e:
            print(f"Error adding customer: {e}")
        finally:
            cursor.close()

    def get_customer(self, customer_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Customer WHERE CustomerID = ?", (customer_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return Customer(*result)
        return None

    def applyLoan(self, loan):
        try:
            cursor = self.connection.cursor()
            confirm = input(
                "Are you sure you want to apply for the loan? (Yes/No): "
            ).lower()
            if confirm == "yes":
                cursor.execute(
                    "INSERT INTO Loan (LoanID, CustomerID, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        loan.get_loan_id(),
                        loan.get_customer().get_customer_id(),
                        loan.get_principal_amount(),
                        loan.get_interest_rate(),
                        loan.get_loan_term(),
                        loan.get_loan_type(),
                        loan.get_loan_status(),
                    ),
                )
                self.connection.commit()
                print("Loan applied successfully!")
            else:
                print("Loan application canceled.")
        except Exception as e:
            print(f"Error applying for loan: {e}")
        finally:
            cursor.close()

    def calculateInterest(self, loanId):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT PrincipalAmount, InterestRate, LoanTerm FROM Loan WHERE LoanID = ?",
                (loanId,),
            )
            loan_data = cursor.fetchone()
            if loan_data:
                principal_amount, interest_rate, loan_term = loan_data
                interest = (principal_amount * interest_rate * loan_term) / 12
                return interest
            else:
                raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        except InvalidLoanException as e:
            raise e
        except Exception as e:
            print(f"Error calculating interest: {e}")
        finally:
            cursor.close()

    def loanStatus(self, loanId):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT CreditScore FROM Customer WHERE CustomerID = (SELECT CustomerID FROM Loan WHERE LoanID = ?)",
                (loanId,),
            )
            credit_score = cursor.fetchone()[0]
            if credit_score > 650:
                cursor.execute(
                    "UPDATE Loan SET LoanStatus = 'Approved' WHERE LoanID = ?",
                    (loanId,),
                )
                self.connection.commit()
                return "Loan approved!"
            else:
                cursor.execute(
                    "UPDATE Loan SET LoanStatus = 'Rejected' WHERE LoanID = ?",
                    (loanId,),
                )
                self.connection.commit()
                return "Loan rejected due to low credit score."
        except Exception as e:
            print(f"Error updating loan status: {e}")
        finally:
            cursor.close()

    def calculateEMI(self, loanId):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT PrincipalAmount, InterestRate, LoanTerm FROM Loan WHERE LoanId = ?",
                (loanId,),
            )
            loan_data = cursor.fetchone()
            if loan_data:
                principal_amount, interest_rate, loan_term = loan_data
                r = interest_rate / (12 * 100)  # Monthly interest rate
                emi = (principal_amount * r * (1 + r) ** loan_term) / (
                    (1 + r) ** loan_term - 1
                )
                return emi
            else:
                raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        except InvalidLoanException as e:
            raise e
        except Exception as e:
            print(f"Error calculating EMI: {e}")
        finally:
            cursor.close()

    def loanRepayment(self, loanId, amount):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT PrincipalAmount, InterestRate, LoanTerm FROM Loan WHERE LoanID = ?",
                (loanId,),
            )
            loan_data = cursor.fetchone()
            if loan_data:
                principal_amount = Decimal(loan_data[0])
                interest_rate = Decimal(loan_data[1])
                loan_term = int(loan_data[2])

                r = interest_rate / Decimal(
                    12 * 100
                )  # Monthly interest rate as Decimal
                emi = (principal_amount * r * (1 + r) ** loan_term) / (
                    (1 + r) ** loan_term - 1
                )

                no_of_emi = int(Decimal(amount) / emi)
                if Decimal(amount) >= emi:
                    cursor.execute(
                        "UPDATE Loan SET LoanStatus = 'Paid' WHERE LoanID = ?",
                        (loanId,),
                    )
                    self.connection.commit()
                    return f"{no_of_emi} EMIs paid successfully."
                else:
                    return "Amount is less than a single EMI. Repayment rejected."
            else:
                raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        except InvalidLoanException as e:
            raise e
        except Exception as e:
            print(f"Error processing loan repayment: {e}")
        finally:
            cursor.close()

    def getAllLoan(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Loan")
            loans = cursor.fetchall()
            formatted_loans = []
            for loan in loans:
                formatted_loan = (
                    loan[0],
                    loan[1],
                    float(loan[2]),
                    float(loan[3]),
                    loan[4],
                    loan[5],
                    loan[6],
                )
                formatted_loans.append(formatted_loan)
            return formatted_loans
        except Exception as e:
            print(f"Error fetching all loans: {e}")
        finally:
            cursor.close()

    def getLoanById(self, loanId):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Loan WHERE LoanID = ?", (loanId,))
            loans = cursor.fetchall()
            formatted_loans = []
            for loan in loans:
                formatted_loan = (
                    loan[0],
                    loan[1],
                    float(loan[2]),
                    float(loan[3]),
                    loan[4],
                    loan[5],
                    loan[6],
                )
                formatted_loans.append(formatted_loan)
            return formatted_loans
        except InvalidLoanException as e:
            raise e
        except Exception as e:
            print(f"Error fetching loan by ID: {e}")
        finally:
            cursor.close()
