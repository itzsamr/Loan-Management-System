from dao.ILoanRepositoryImpl import ILoanRepositoryImpl
from exception.InvalidLoanException import InvalidLoanException


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
        # Implement apply loan functionality
        pass

    def calculate_interest(self):
        # Implement calculate interest functionality
        pass

    def check_loan_status(self):
        # Implement check loan status functionality
        pass

    def calculate_emi(self):
        # Implement calculate EMI functionality
        pass

    def make_loan_repayment(self):
        # Implement make loan repayment functionality
        pass

    def get_all_loans(self):
        # Implement get all loans functionality
        pass

    def get_loan_by_id(self):
        # Implement get loan by ID functionality
        pass
