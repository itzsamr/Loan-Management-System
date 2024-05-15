from dao import *
from entity import *
from util import *
from exception import *


class LoanManagement:
    def __init__(self):
        self.loan_repo = ILoanRepositoryImpl()

    def main(self):
        while True:
            print("\n====== Loan Management System Menu ======")
            print("1. Apply for Loan")
            print("2. Calculate Interest")
            print("3. Check Loan Status")
            print("4. Calculate EMI")
            print("5. Make Loan Repayment")
            print("6. Get All Loans")
            print("7. Get Loan by ID")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.apply_loan()
            elif choice == "2":
                self.calculate_interest()
            elif choice == "3":
                self.check_loan_status()
            elif choice == "4":
                self.calculate_emi()
            elif choice == "5":
                self.make_loan_repayment()
            elif choice == "6":
                self.get_all_loans()
            elif choice == "7":
                self.get_loan_by_id()
            elif choice == "8":
                print("Exiting Loan Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def apply_loan(self):
        loan_id = int(input("Enter Loan ID: "))
        customer_id = int(input("Enter Customer ID: "))
        principal_amount = float(input("Enter Principal Amount: "))
        interest_rate = float(input("Enter Interest Rate: "))
        loan_term = int(input("Enter Loan Term (in months): "))
        loan_type = input("Enter Loan Type (CarLoan/HomeLoan): ")
        customer_credit_score = int(input("Enter Customer Credit Score: "))

        loan = Loan(
            loan_id,
            customer_id,
            principal_amount,
            interest_rate,
            loan_term,
            loan_type,
            "Pending",
        )
        try:
            self.loan_repo.applyLoan(loan)
            self.loan_repo.loanStatus(loan_id, customer_credit_score)
            print("Loan applied successfully!")
        except InvalidLoanException as e:
            print(e)

    def calculate_interest(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            interest = self.loan_repo.calculateInterest(loan_id)
            print(f"Interest for Loan ID {loan_id}: {interest}")
        except InvalidLoanException as e:
            print(e)

    def check_loan_status(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            status_message = self.loan_repo.loanStatus(loan_id)
            print(f"Loan Status: {status_message}")
        except InvalidLoanException as e:
            print(e)

    def calculate_emi(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            emi = self.loan_repo.calculateEMI(loan_id)
            print(f"EMI for Loan ID {loan_id}: {emi}")
        except InvalidLoanException as e:
            print(e)

    def make_loan_repayment(self):
        loan_id = int(input("Enter Loan ID: "))
        amount = float(input("Enter Repayment Amount: "))
        try:
            repayment_message = self.loan_repo.loanRepayment(loan_id, amount)
            print(repayment_message)
        except InvalidLoanException as e:
            print(e)

    def get_all_loans(self):
        try:
            loans = self.loan_repo.getAllLoan()
            if loans:
                print("All Loans:")
                for loan in loans:
                    print(loan)
            else:
                print("No loans found.")
        except InvalidLoanException as e:
            print(e)

    def get_loan_by_id(self):
        loan_id = int(input("Enter Loan ID: "))
        try:
            loan = self.loan_repo.getLoanById(loan_id)
            print(f"Loan Details for Loan ID {loan_id}: {loan}")
        except InvalidLoanException as e:
            print(e)
