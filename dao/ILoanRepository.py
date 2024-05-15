from abc import ABC, abstractmethod


class ILoanRepository(ABC):
    @abstractmethod
    def applyLoan(self, loan):
        pass

    @abstractmethod
    def calculateInterest(self, loan_id):
        pass
