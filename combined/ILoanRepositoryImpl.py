from ILoanRepository import ILoanRepository
from .DBConnection import DBConnUtil
from InvalidLoanException import InvalidLoanException


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def applyLoan(self, loan):
        try:
            cursor = self.connection.cursor()
            confirm = input(
                "Are you sure you want to apply for the loan? (Yes/No): "
            ).lower()
            if confirm == "yes":
                cursor.execute(
                    "INSERT INTO Loans (loanId, customerId, principalAmount, interestRate, loanTerm, loanType, loanStatus) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        loan.loanId,
                        loan.customer.customerId,
                        loan.principalAmount,
                        loan.interestRate,
                        loan.loanTerm,
                        loan.loanType,
                        "Pending",
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
                "SELECT principalAmount, interestRate, loanTerm FROM Loans WHERE loanId = ?",
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
                "SELECT creditScore FROM Customers WHERE customerId = (SELECT customerId FROM Loans WHERE loanId = ?)",
                (loanId,),
            )
            credit_score = cursor.fetchone()[0]
            if credit_score > 650:
                cursor.execute(
                    "UPDATE Loans SET loanStatus = 'Approved' WHERE loanId = ?",
                    (loanId,),
                )
                self.connection.commit()
                return "Loan approved!"
            else:
                cursor.execute(
                    "UPDATE Loans SET loanStatus = 'Rejected' WHERE loanId = ?",
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
                "SELECT principalAmount, interestRate, loanTerm FROM Loans WHERE loanId = ?",
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
                "SELECT principalAmount, interestRate, loanTerm FROM Loans WHERE loanId = ?",
                (loanId,),
            )
            loan_data = cursor.fetchone()
            if loan_data:
                principal_amount, interest_rate, loan_term = loan_data
                r = interest_rate / (12 * 100)  # Monthly interest rate
                emi = (principal_amount * r * (1 + r) ** loan_term) / (
                    (1 + r) ** loan_term - 1
                )
                no_of_emi = int(amount / emi)
                if amount >= emi:
                    cursor.execute(
                        "UPDATE Loans SET noOfEMI = ?, loanStatus = 'Paid' WHERE loanId = ?",
                        (
                            no_of_emi,
                            loanId,
                        ),
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
            cursor.execute("SELECT * FROM Loans")
            loans = cursor.fetchall()
            return loans
        except Exception as e:
            print(f"Error fetching all loans: {e}")
        finally:
            cursor.close()

    def getLoanById(self, loanId):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Loans WHERE loanId = ?", (loanId,))
            loan = cursor.fetchone()
            if loan:
                return loan
            else:
                raise InvalidLoanException(f"Loan with ID {loanId} not found.")
        except InvalidLoanException as e:
            raise e
        except Exception as e:
            print(f"Error fetching loan by ID: {e}")
        finally:
            cursor.close()
