from ILoanRepository import ILoanRepository
from DBConnUtil import DBConnUtil


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.getConnection()
