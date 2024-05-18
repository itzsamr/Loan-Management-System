from abc import ABC, abstractmethod


class ILoanRepository(ABC):
    @abstractmethod
    def applyLoan(self, loan):
        pass

    @abstractmethod
    def calculateInterest(self, loanId):
        pass

    @abstractmethod
    def loanStatus(self, loanId):
        pass

    @abstractmethod
    def calculateEMI(self, loanId):
        pass

    @abstractmethod
    def loanRepayment(self, loanId, amount):
        pass

    @abstractmethod
    def getAllLoan(self):
        pass

    @abstractmethod
    def getLoanById(self, loanId):
        pass

    @abstractmethod
    def customer_exists(self, customer_id):
        pass

    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def get_customer(self, customer_id):
        pass
