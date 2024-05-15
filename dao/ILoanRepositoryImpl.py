from abc import ABC, abstractmethod
from .ILoanRepository import ILoanRepository
from util.DBConnection import DBConnUtil


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def applyLoan(self, loan):
        pass

    def calculateInterest(self, loanId):
        pass

    def loanStatus(self, loanId):
        pass

    def calculateEMI(self, loanId):
        pass

    def loanRepayment(self, loanId, amount):
        pass

    def getAllLoan(self):
        pass

    def getLoanById(self, loanId):
        pass
