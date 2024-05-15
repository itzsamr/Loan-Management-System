from ILoanRepository import ILoanRepository
from util.DBConnection import DBConnUtil


class ILoanRepositoryImpl(ILoanRepository):
    def __init__(self):
        self.connection = DBConnUtil.getConnection()
